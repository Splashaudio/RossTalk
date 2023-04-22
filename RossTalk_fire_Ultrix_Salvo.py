#sends RossTalk commands to Ultrix

import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('xxx.xxx.xxx.xxx', 7788)  #replace xxx.xxx.xxx.xxx with ip address of Ulrix

sock.connect(server_address)


data = b'GPI 03\r\n'  #fire number salvo 3

sock.sendall(data)

# Close the socket
sock.close()
