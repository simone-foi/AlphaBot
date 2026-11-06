import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.0.202', 5000))

while True:
    comando = input().strip().lower()
    if not comando:
        continue
    client_socket.sendall(comando.encode('utf-8'))
    
    if comando == 'q':
        break

client_socket.close()