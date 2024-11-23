from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName,serverPort))
sentence = input('Input lowercase sentence:') # works only in Python 3.x
# For Python 2.x use: message = raw_input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024).decode()
print('From Server:', modifiedSentence) 
clientSocket.close()
