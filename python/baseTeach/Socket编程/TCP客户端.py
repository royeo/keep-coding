from socket import *

HOST = ''
PORT = 11561
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        continue
    tcpCliSock.send(data.encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print(data)

tcpCliSock.close()