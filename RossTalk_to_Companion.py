#sends RossTalk commands.
#Sending to Bitfocus Companion for the moment until studio install is finished
#edit

import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('localhost', 7788)
sock.connect(server_address)

# Send the data
data = b'CC 1:8'  #send RossTalk to triger Companion. Triggers Bank 1 button 8
sock.sendall(data)

# Receive the response
response = sock.recv(1024)

# Print the response
print(response)

# Close the socket
sock.close()
