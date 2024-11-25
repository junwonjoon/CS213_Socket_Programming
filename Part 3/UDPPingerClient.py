# UDPPingerClient.py;
# Reference: Kurose and Ross textbook, 7th ed.
# Author(s): Nicholas Harris

from socket import *
import time
import sys

def calculate_rtt(client_socket, server_name, server_port, message):
    start_time = time.time()
    client_socket.sendto(message.encode(), (server_name, server_port))
    client_socket.settimeout(1)
    try:
        modified_message, server_address = client_socket.recvfrom(2048)
    except timeout:
        print("Request timed out")
        return None 
    end_time = time.time()
    return (end_time - start_time), modified_message.decode()

def main():
    server_name = sys.argv[1] 
    server_port = int(sys.argv[2])

    # Create a UDP socket
    client_socket = socket(AF_INET, SOCK_DGRAM)

    # Request the user for how many messages they would like to send
    n = int(input("Enter how many messages you would like to send (typically 12): "))

    # Initialize variables for RTT statistics
    total_rtt = 0.0
    lowest_rtt = None
    highest_rtt = None
    timed_out = 0

    for i in range(n):
        message = input("Input lowercase sentence for packet %d: " %(i+1))
        rtt_result = calculate_rtt(client_socket, server_name, server_port, message)
        if rtt_result is None:
            timed_out += 1
            continue 
        current_rtt, modified_message = rtt_result
        print("Message received from server: " + modified_message)
        if lowest_rtt is None or current_rtt < lowest_rtt:
            lowest_rtt = current_rtt
        if highest_rtt is None or current_rtt > highest_rtt:
            highest_rtt = current_rtt
        total_rtt += current_rtt
        print("The RTT for packet %d is: %.3f s" %(i+1, current_rtt))

    # Print RTT statistics
    if lowest_rtt is not None:  # Ensure at least one successful connection occurred
        print("\nRTT Statistics:")
        print("Minimum RTT: %.3f s" %(lowest_rtt))
        print("Average RTT: %.3f s" %(total_rtt/(n - timed_out)))
        print("Maximum RTT: %.3f s" %(highest_rtt))
        packet_loss_rate = timed_out / n
        print(f"The packet loss rate is {packet_loss_rate:.0%}")
    else:
        print("\nNo successful connections were made.")
    client_socket.close()

if __name__ == "__main__":
    main()
