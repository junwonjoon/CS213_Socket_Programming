MAX_MESSAGE_LENGTH = 1024 #bytes 
from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName,serverPort))
sentence = input('Input lowercase sentence:')
if len(sentence) > MAX_MESSAGE_LENGTH:
  print(f"Error: Message length is greater than the max length")
  clientSocket.close()
  exit()
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024).decode()
print('From Server:', modifiedSentence) 
clientSocket.close()
