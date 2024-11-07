from socket import *
serverName = 'localhost'
serverPort = 8000
clientSocket = socket(AF_INET, SOCK_DGRAM) 
message = input('Input lowercase sentence:') # works only in Python 3.x
# For Python 2.x use: message = raw_input('Input lowercase sentence:')
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print("Server says: %s" % modifiedMessage)
clientSocket.close()
