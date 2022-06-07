import socket
import os
from _thread import *


ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostIP = '127.3.4.1'
portNo = 54321

threadCount = 0
clientBuffer = []
ServerSocket.bind((hostIP, portNo))

print('Server is Listening.....')
ServerSocket.listen(5)

def threaded_client(connection):
    connection.send(str.encode('Welcome to the server'))
    while True:
        data = connection.recv(2048)
        reply = data.decode('utf-8')
        if not data:
            break
        for client in clientBuffer:client.sendall(str.encode(reply))
    connection.close()


while True:
    client, address = ServerSocket.accept()
    print('Server is connected to ' + address[0] + ': ' + str(address[1]))
    start_new_thread(threaded_client, (client,))
    threadCount +=1
    print('Thread number: ' + str(threadCount))
    clientBuffer.append(client)

ServerSocket.close()











