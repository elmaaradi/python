import socket

s = socket.socket()
host = '10.22.1.160'
port = 12221

s.connect((host, port))
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    print(c.recv(1024))
    output = input("Enter something for the server: ")
    s.sendall(output.encode('utf-8'))
    print(s.recv(1024))