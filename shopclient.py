from socket import *

serverName = "127.0.0.1"
serverPort = 12001

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

def mainf(body):
    clientSocket.send(body.encode())
    serverReply = clientSocket.recv(2048)
    reply=eval(serverReply.decode())
    return reply

