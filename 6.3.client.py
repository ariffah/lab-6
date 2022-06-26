import sys
import socket

clientSocket = socket.socket()
host = '192.168.56.104'
port = 8888

print("Waiting for connection")
try:
    clientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

response = clientSocket.recv(1024)
print(response.decode())

while True:
    option = input('Choose mathematical function, A -Logarithmic, B -Square Root, C -Exponential or Q to quit: ')

    if option == 'A' or option == 'B' or option == 'C':
        value = input("Enter a value: ")
        option = option + ":" + value
        clientSocket.send(str.encode(option))
        response = clientSocket.recv(1024)
        print(response.decode("utf-8"))

    elif option == 'Q':
        print("Quiting app.")
        clientSocket.send(str.encode(option))
        sys.exit()
        
    else:
        print("Invalid input! Enter only A,B,C")
        print("Please try again.")
        option = "0"
        clientSocket.send(str.encode(option))
        response = clientSocket.recv(1024)
        print('***********')

clientSocket.close()
