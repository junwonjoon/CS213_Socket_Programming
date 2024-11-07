# UDPPingerServer.py;
# Reference: Kurose and Ross textbook, 7th ed.

# We will need the following modules for sockets and to randomly select packets to lose
import random
from socket import *

# Create a UDP socket (notice the use of SOCK_DGRAM for UDP packets)
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and a port number to socket
serverSocket.bind(('', 12000))

print("UDP Pinger Server is waiting for pings to pong!")
while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)

    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(2046)
    
    # Capitalize the message from the client
    message = message.upper()
    
    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 3:
        continue
    
    # Otherwise, the server responds
    serverSocket.sendto(message, address)
