# UDPPingerServer.py;
# Reference: Kurose and Ross textbook, 7th ed.
# Author(s): Nicholas Harris

import time
import random
from socket import *

# Blocked IP addresses from communicating with the server
blacklisted = []
# blacklisted.append("") Uncomment and add IP addresses to blacklist them.

# Creates a UDP Socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Since the server is opening a socket on its own host, a blank IP address/hostname is acceptable. 
# Assigns an IP address and a port number to the socket
serverSocket.bind(('', 12000)) 

client_address = None
client_message = None

print("UDP Pinger Server is waiting for pings to pong!")
while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    
    # Generates a random number between 0.300 and 0.500 up to 3 decimal places. This will be used as a random delay. 
    delay = round(random.uniform(0.300, 0.500), 3)

    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(2048)
    
    if client_message is None: 
    	client_message = message
    
    if client_address is None: 
    	client_address = address
    elif client_address != address: 
    	print("Multiple simultaneous sessions attempted. Request from %s on port %d has been blocked." %(address[0], address[1]))
    	continue
    
    if client_address[0] in blacklisted: 
    	print("Address blacklisted: %s; Access denied." %(client_address[0]))
    	continue 
    	
    # Capitalize the message from the client
    client_message = client_message.upper()
    
    time.sleep(delay)
    
    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 3:
        continue
    
    # Otherwise, the server responds
    serverSocket.sendto(client_message, client_address)
    client_address = None
    client_message = None
