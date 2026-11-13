import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.202", 5000))
print("Ricordati che password e username sono case sensitive")

while True:
    cmd = input("user;pass --> ")
    s.sendall((cmd + "\n").encode())
    
    if cmd.upper() == "EXIT":
        break

    data = s.recv(4096)
    print(data.decode().strip())

s.close()