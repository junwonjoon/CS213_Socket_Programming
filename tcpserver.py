from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind(('',serverPort)) 
serverSocket.listen(1)
print('The server is ready to receive') 
while 1:
 connectionSocket, addr = serverSocket.accept() 
 sentence = connectionSocket.recv(1024) 
 capitalizedSentence = sentence.upper() 
 connectionSocket.send(capitalizedSentence)
 print("Finished serving %s at port#: %s" % (addr[0], addr[1]))  
 connectionSocket.close()
