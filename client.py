from socket import *
import ssl
import json

def sendmessage(ch, uname, pwd):
    serverName = "127.0.0.1"
    serverPort = 12000

    # Wrap the socket with SSL
    ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ssl_context.check_hostname = False
    ssl_context.load_verify_locations('C:\\Users\\thani\\domain.crt')  # Assuming you have the server certificate

    clientSocket = ssl_context.wrap_socket(socket(AF_INET, SOCK_STREAM))

    clientSocket.connect((serverName, serverPort))

    msg = ''
    if ch == 0:
        msg = {"type": 0, "uname": uname, "pwd": pwd}
        msg = json.dumps(msg)
        clientSocket.send(msg.encode())
        serverReply = clientSocket.recv(2048)
        reply = eval(serverReply.decode())
        # print(reply)

    else:
        msg = {"type": 1, "uname": uname, "pwd": pwd}
        msg = json.dumps(msg)
        clientSocket.send(msg.encode())
        serverReply = clientSocket.recv(2048)
        reply = eval(serverReply.decode())
        # print(reply)

    clientSocket.close()

    return reply

