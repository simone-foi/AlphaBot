import socket
import time
import datetime

INTERVALLO = 2

lista_stazioni = [1, 2, 3, 4, 5]
lista_potenze = [30, 55, 90, 70, 95]
lista_temperature = [100, 180, 300, 225, 360]

for st, p, t in zip(lista_stazioni, lista_potenze, lista_temperature):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 5050))
    stringa = f"{st};{p};{t};{datetime.datetime.now()}"
    s.sendall(stringa.encode())
    risposta = s.recv(1024).decode()
    allarme = s.recv(1024).decode().strip()
    if allarme:
        risposta = risposta + " - " + allarme
    print(f"Stazione {st} -> {risposta}")
    time.sleep(INTERVALLO)
    s.close()