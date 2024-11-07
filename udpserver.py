from socket import *
serverPort = 8000
serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind(("", serverPort))
print("The server is ready to receive") 
while 1:
 message, clientAddress = serverSocket.recvfrom(2048)
 modifiedMessage = message.upper() 
 serverSocket.sendto(modifiedMessage, clientAddress)
 # print("Finished serving %s at port#: %s" % (clientAddress[0], clientAddress[1]))
 print("Completed service for:", clientAddress)
