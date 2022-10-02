from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = """GET / HTTP/1.1
Host: example.com 
Connection: close \r\n"""

clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())
clientSocket.close()

