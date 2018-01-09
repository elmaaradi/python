import socket         

s = socket.socket()        
host = '10.22.1.30'
port = 12221               
s.bind((host, port))   

s.listen(5)

while True:
   c, addr = s.accept()
   print('Got connection from', addr)
   print(c.recv(1024))
   q = input("Enter something to this client: ")
   s.sendall(q.encode('utf-8'))