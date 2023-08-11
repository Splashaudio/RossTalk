#sends RossTalk commands to Carbonite to cut to input on program buss

import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('xxx.xxx.xxx.xxx', 7788)  #replace xxx.xxx.xxx.xxx with ip address of Carbonite

sock.connect(server_address)

# Send the data

#data = b'MECUT ME:P/P\r\n'  #sends CUT to Carbonite
#data = b'XPT AUX:2:IN:3\r\n'   #cuts aux 2 to input 3

data = b'XPT ME:P/P:PGM:IN:2\r\n'   #cut to and input on the ME P/P row


sock.sendall(data)

# Receive the response
#response = sock.recv(1024)

# Print the response
#print(response)

# Close the socket
sock.close()
