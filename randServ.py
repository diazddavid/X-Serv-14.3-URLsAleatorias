#!/usr/bin/python3

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 12345))

mySocket.listen(5)

while True:
    print('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print('HTTP request received:')
    print(recvSocket.recv(1024))
    nextDirection = str(random.randrange(100000000000))
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                    "<html><body><h1> Hola. <a href=" + nextDirection +
                    ">Dame otra </a> </h1></body></html>" +
                    "\r\n", "utf-8"))
    recvSocket.close()
