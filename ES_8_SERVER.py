import socket
import threading
import sqlite3

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("0.0.0.0", 5050))
s.listen(10)

semaforo = threading.Semaphore(10)

def gestisci_client(conn, addr):
    semaforo.acquire()
    dati = conn.recv(1024).decode().strip().split(";")
    id_stazione, potenza, temperatura, data_ora = int(dati[0]), int(dati[1]), int(dati[2]), dati[3]
    db = sqlite3.connect("impianti.db")
    cur = db.cursor()
    cur.execute("SELECT potenza_nominale, temp_massima FROM centrali WHERE id_stazione = ?", (id_stazione,))
    potenza_nominale, temp_massima = cur.fetchone()

    if potenza / potenza_nominale * 100 < 50:
        risposta = "OK-BASSA-PRODUZIONE  ---  "
    elif potenza / potenza_nominale * 100 >= 50 and potenza / potenza_nominale * 100 < 90:
        risposta = "OK-PRODUZIONE-REGOLARE  ---  "
    else:
        risposta = "OK-PRODUZIONE-OTTIMALE  ---  "
    conn.sendall(risposta.encode())

    if temperatura > temp_massima:
        rispostaDB = "ALLARME-TEMPERATURA\n"
        cur1 = db.cursor()
        cur1.execute("INSERT INTO AllarmiTemperature ('id', 'temp_rilevata', 'data') VALUES (?, ?, ?)", (id_stazione, temperatura, data_ora))
        db.commit()
        conn.sendall(rispostaDB.encode())

    db.close()
    conn.close()
    semaforo.release()

while True:
    conn, addr = s.accept()
    t = threading.Thread(target=gestisci_client, args=(conn, addr))
    t.start()