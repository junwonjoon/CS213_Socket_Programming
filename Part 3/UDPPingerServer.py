# UDPPingerServer.py;
# Reference: Kurose and Ross textbook, 7th ed.

import time
import random
from socket import *

# Creates a UDP Socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assigns an IP address and a port number to the socket
serverSocket.bind(('', 12000)) 

print("UDP Pinger Server is waiting for pings to pong!")
while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    
    # Generates a random number between 300 and 500 milliseconds. 
    # Here it is converted into seconds for ease of use. 
    delay_int = random.randint(300, 500) 
    delay = delay_int / 1000

    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(2046)
    
    # Capitalize the message from the client
    message = message.upper()
    
    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 3:
        continue
    
    # Otherwise, the server responds
    time.sleep(delay)
    serverSocket.sendto(message, address)
