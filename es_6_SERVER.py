import socket
import sqlite3

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 5000))
s.listen(1)

conn_socket, addr = s.accept()

while True:
    data = conn_socket.recv(4096)
    if not data:
        break
    
    messaggio = data.decode().strip()
    if messaggio.upper() == "EXIT":
        break

    parti = messaggio.split(";")
    db = sqlite3.connect("Utenti.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM Login WHERE NomeUtente = ? AND Password = ?", (parti[0], parti[1]))
    risultato = cur.fetchone()
    db.close()

    if risultato:
        risposta = "LOGIN OK\n"
    else:
        risposta = "LOGIN FALLITO\n"

    conn_socket.sendall(risposta.encode())

conn_socket.close()
s.close()