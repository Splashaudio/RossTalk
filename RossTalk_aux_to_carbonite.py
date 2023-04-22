#sends RossTalk commands to Carbonite Aux Buss

import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('xxx.xxx.xxx.xxx', 7788)  #replace xxx.xxx.xxx.xxx with ip address of Ulrix

sock.connect(server_address)


data = b'XPT AUX:2:IN:3\r\n'  #cut aux 2 to input 3
sock.sendall(data)

sock.close()
