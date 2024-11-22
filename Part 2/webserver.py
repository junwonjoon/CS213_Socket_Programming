# webserver_skeleton.py: Skeleton Python code for the Web Server -- Kurose and Ross textbook (7th ed.)
# This code makes use of Python socket library module, exceptions, and file I/O

#import socket module
from socket import *
import sys # sys module needed to terminate the program

#Prepare a TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

#FILL IN START

#FILL IN END

while True:
#Establish the connection
    print('The server is ready to receive')
# Set up a new connection from the client
    connectionSocket, addr = #Fill in start             #Fill in end

# If an exception occurs during the execution of try clause
# the rest of the clause is skipped
# If the exception type matches the word after except
# the except clause is executed
try:
    # Receives the HTTP request message from the client
    message = #FILL IN START    #FILL IN END
        
    # Extract the path of the requested object from the message
    # The path is the second part of HTTP header, identified by [1]
    filename = message.split()[1] # Note: these are Python file operations
    print('File name is:', filename.encode("UTF-8"))

    # Because the extracted path of the HTTP request includes                                                 
    # a character '/', we read the path from the second character 
    f = open(filename[1:])
    
    # Store the entire content of the requested file in a temporary buffer
    outputdata = #FILL IN START     #FILL IN END
    
    #Send one HTTP response header line into socket
    #FILL IN START

    
    #FILL IN END
    
    #Send the content of the requested file to the connection socket
    for i in range(0, len(outputdata)):
        #FILL IN START
        
    #FILL IN END

    # Close the client connection socket
    connectionSocket.close()

except IOError:
    #Send HTTP response message for file not found
    #FILL IN START
    #FILL IN END

    #Close the client connection socket
    #FILL IN START
    #FILL IN END

serverSocket.close()
sys.exit()
