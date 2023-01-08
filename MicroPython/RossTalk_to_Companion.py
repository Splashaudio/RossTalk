#sends RossTalk command to Companion. Just used as a test before installing Ross router.
#Runs on Raspberry Pi pico
#edit
#another
import time
import network
import usocket

#------------
#   setting up wifi
ssid = 'xxxxxx' #network SSDI
password = 'XXXXXX' #passcode
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
 
# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )




#---------------------
    #seting up TCP Send
# Create a TCP/IP socket
sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('192.168.0.92', 7788)
sock.connect(server_address)

# Send the data
# data = b'CC 1:8'
# sock.send(data)

# Receive the response
#response = sock.recv(1024)

# Print the response
#print(response)

while True:
    data = b'CC 1:8'
    sock.send(data)
    time.sleep(1)


# Close the socket
sock.close()
