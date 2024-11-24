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

# Sends n packets from the client to the server.
n = int(input("Enter how many messages you would like to send (default is 12): "))
for i in range(n): 
    # Retrieves input from the user which will be sent to the UDP Server program
    message = input('Input lowercase sentence for packet %d:'%(i))
    clientSocket.settimeout(1)
    count = 0
   
    try: 
        cRTT = RTT(serverName, serverPort, message) 
        RTT = cRTT * 1000
        if count == 0: 
            global lowest = RTT
            global highest = RTT
        else:     
            if RTT >= highest: 
                highest = RTT
            if RTT <= lowest: 
                lowest = RTT
        global total += RTT
    
    except socket.timeout: 
        print("Request timed out.")

# Prints the modified message
print(modifiedMessage.decode())

# Prints finalized RTT statistics
print("RTT Statistics: ")    
print("Minimum: %.3lf; Average: %.3lf; Maximum: %.3lf" %(lowest, (total/12), highest))    

# Closes the socket
clientSocket.close()
