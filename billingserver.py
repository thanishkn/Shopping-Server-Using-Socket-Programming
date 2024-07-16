from socket import *
import csv
import threading
from orders import *

def handle_client(connectionSocket, addr):
    print("Connected to:", addr,end=',')

    message = connectionSocket.recv(2048)
    if not message:
        connectionSocket.close()
        return
    
    bill = eval(message.decode())
    print("Recieved Request Body=",bill)
    type = bill.pop(0)
    reply= ""

    if type==0:
        uname = bill.pop(0)
        print(bill)
        userbill = []
        userbill.append(uname)
        userbill.append(bill)
        update(str(userbill))

        netamt = 0

        for i in bill:
            netamt+= i[1]*i[2]
        
        
        reply=str(netamt)
    
    else:
        uname = bill.pop(0)
        f = open('Python Project\\MiniProject\\orders.csv','r')
        rows = csv.reader(f)
        orders=[]
        for i in list(rows):
            if i != []:
                ele = i.pop(0)
                print(ele)
                if ele == uname:
                    orders.append(i)
        reply= str(orders)
    
    connectionSocket.send(reply.encode())
    connectionSocket.close()

    


serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)  # Increased the backlog to handle multiple connections


print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()

    # Create a new thread to handle each client
    client_handler = threading.Thread(target=handle_client, args=(connectionSocket, addr))
    client_handler.start()

