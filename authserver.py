from socket import *
import csv
import json
import threading
import ssl

def handle_client(connectionSocket, addr):
    print("Connected to:", addr, end=',')

    message = connectionSocket.recv(2048)
    if not message:
        connectionSocket.close()
        return
    
    msg_data = json.loads(message.decode())
    type, ruser, rpwd = msg_data["type"], msg_data["uname"], msg_data["pwd"]
    print("Received Request Body =", type, ruser, rpwd)

    reply = False
    if type == 0:
        with open("./Python Programs/MiniProject/credentials.csv", 'r') as f:
            rows = csv.reader(f)
            for i in rows:
                uname, pwd = tuple(i)
                if uname == ruser and pwd == rpwd:
                    reply = True
                    break
    else:
        with open("./Python Programs/MiniProject/credentials.csv", 'a') as f:
            csvw = csv.writer(f)
            csvw.writerow([ruser, rpwd])
            reply = True

    reply = {"reply": str(reply)}
    connectionSocket.send(json.dumps(reply).encode())
    connectionSocket.close()

# Main server code
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)

# Wrap the socket with SSL
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile='C:\\Users\\thani\\domain.crt', keyfile='C:\\Users\\thani\\domain.key',password='openssl123')


ssl_serverSocket = ssl_context.wrap_socket(serverSocket, server_side=True)

print("The server is ready to receive")

while True:
    try:
        connectionSocket, addr = ssl_serverSocket.accept()

        # Create a new thread to handle each client
        client_handler = threading.Thread(target=handle_client, args=(connectionSocket, addr))
        client_handler.start()

    except ssl.SSLError as e:
        print(f"SSL error: {e}")
        # Handle SSL errors appropriately
