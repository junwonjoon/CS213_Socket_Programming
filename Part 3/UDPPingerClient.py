# UDPPingerClient.py;
# Reference: Kurose and Ross textbook, 7th ed.
# Author(s): Nicholas Harris

from socket import *
import time

def RTT(serverName, serverPort, message): 
    # Immediately before sending the message, the first timestamp is created.
    start_time = time.time() 
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    # Immediately after receiving the message, the second timestamp is created. 
    end_time = time.time() 
    return str(end_time-start_time)

# Hostname and IP Address for our client
serverName = '' # Insert the server's IP address here (This must be accessible to the client) 
serverPort = 12000

# Creates a UDP Socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Sends 12 packets from the client to the server.
for i in range(12): 
    # Retrieves input from the user which will be sent to the UDP Server program
    message = input('Input lowercase sentence for packet %d:'%(i))
    
    calculated_RTT = RTT(serverName, serverPort, message) 
    RTT_in_ms = calculated_RTT * 1000
    if calculated_RTT >= 1: 
        print("The packet was lost.")     
    else: 
        print("The calculated RTT for Ping %d is "%(i,RTT_in_ms)) 


# Prints the modified message
print(modifiedMessage.decode())

# Closes the socket
clientSocket.close()
