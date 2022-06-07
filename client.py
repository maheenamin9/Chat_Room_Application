import socket
from _thread import *

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostIP = '127.3.4.1'
portNo = 54321

print('Waiting for the connection')
ClientSocket.connect((hostIP, portNo))
Response = ClientSocket.recv(2048)

def recv_threaded_client(connection):
    while True:
        Response = connection.recv(2048)
        print('Responce msg: ' + Response.decode('utf-8'))
    connection.close()

start_new_thread(recv_threaded_client, (ClientSocket,))
while True:
    Inputdata = input('Client saying: ')
    ClientSocket.send(str.encode(Inputdata))

ClientSocket.close()









