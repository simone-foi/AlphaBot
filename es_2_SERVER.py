import socket
from libreria import AlphaBot
import time

robot = AlphaBot()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5000))
server_socket.listen(1)

conn, addr = server_socket.accept()

while True:
    data = conn.recv(1024).decode('utf-8').strip().lower()
    if not data:
        break
        
    if data == 'w':
        robot.forward()
        time.sleep(2)
    elif data == 's':
        robot.backward()
        time.sleep(2)
    elif data == 'a':
        robot.left()
        time.sleep(0.8)
    elif data == 'd':
        robot.right()
        time.sleep(0.4)
    elif data == 'q':
        robot.stop()
        break

robot.cleanup()
server_socket.close()
conn.close()