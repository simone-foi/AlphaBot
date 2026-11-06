import socket
import time
import keyboard

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.0.202', 5000))

ultimo_comando = ""

while True:
    if keyboard.is_pressed('w'):
        comando = 'w'
    elif keyboard.is_pressed('s'):
        comando = 's'
    elif keyboard.is_pressed('a'):
        comando = 'a'
    elif keyboard.is_pressed('d'):
        comando = 'd'
    elif keyboard.is_pressed('q'):
        comando = 'q'
        client_socket.sendall(comando.encode('utf-8'))
        break
    else:
        comando = 'stop'

    if comando != ultimo_comando:
        client_socket.sendall(comando.encode('utf-8'))
        ultimo_comando = comando

    time.sleep(0.05)

client_socket.close()