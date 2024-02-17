# from bluetooth import *
# import sys

 
# port = 19
# # try to connect to the port
# try:
#     sock=BluetoothSocket( RFCOMM )
#     sock.connect(( 'D4:8A:39:34:73:FD' , port))
# except:
#     print ("An error occurred while trying to connect. Exiting...")
#     sys.exit()

# print( "Connected. Type something...")

# # read the data from the port
# data = sock.recv(1000)
# print ("Data received: %s" % data)
# sock.close()

from bluetooth import *

# Address of the Bluetooth device
addr = 'D4:8A:39:34:73:FD'

# Port number for SPP
port = 14

# Create a Bluetooth socket
sock = BluetoothSocket(RFCOMM)

# Connect to the device
sock.connect((addr, port))

# Send some data
sock.send('Hello, world!')

# Receive some data
data = sock.recv(1024)
print('Received:', data)

# Close the connection
sock.close()