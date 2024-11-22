# webserver_skeleton.py: Skeleton Python code for the Web Server -- Kurose and Ross textbook (7th ed.)
# This code makes use of Python socket library module, exceptions, and file I/O

# import socket module
from socket import *
import sys
# Prepare a TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# FILL IN START
serverPort = 8000
serverHost = '127.0.0.1' #localhost also works
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(5)
# FILL IN END

while True:
    # Establish the connection
    print('The server is ready to receive')
    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()  # Fill in start             #Fill in end

    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    try:
        # Receives the HTTP request message from the client
        message = connectionSocket.recv(1024).decode('utf-8')
        # The if statement added by Wonjoon to prevent code from crashing by index out of range error.
        # This checks if message is empty, it restarts the loop when message is empty
        if not message:
            continue
        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]  # Note: these are Python file operations
        print('File name is:', filename.encode("UTF-8"))

        # Because the extracted path of the HTTP request includes
        # a character '/', we read the path from the second character

        f = open(filename[1:])
        # Store the entire content of the requested file in a temporary buffer
        outputdata = f.read()  # FILL IN START     #FILL IN END
        f.close()

        # Send one HTTP response header line into socket
        # FILL IN START
        header = "HTTP/1.1 200 OK\r\n"
        header += "Content-Type: text/html\r\n"
        header += f"Content-Length: {len(outputdata)}\r\n"
        header += "\r\n"
        connectionSocket.send(header.encode())
        # FILL IN END

        # Send the content of the requested file to the connection socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        # Close the client connection socket
        connectionSocket.close()
    except IOError:
        # Send HTTP response message for file not found
        error_response = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/html\r\n"
            "Content-Length: 47\r\n"
            "\r\n"
            "<html><body><h1>404 Not Found</h1></body></html>"
        )
        connectionSocket.sendall(error_response.encode())
    # Close the client connection socket
        connectionSocket.close()
serverSocket.close()
sys.exit()
