import bluetooth

# Replace these values with your actual Bluetooth MAC address and SIM access port
MAC_ADDRESS = '20:CD:6E:35:15:68'
SIM_ACCESS_PORT = 16

# Connect to the Bluetooth device
bd_addr = MAC_ADDRESS
port = SIM_ACCESS_PORT
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))
# Send AT commands to dial a number
number_to_call = '+919440903979'  # Replace with the desired phone number

# AT command to enter command mode
sock.send(b'AT\r')
# AT command to dial the number
dial_command = f'ATD{number_to_call};\r'.encode('ascii')
sock.send(dial_command)
# Wait for a few seconds to allow the call to connect
import time
time.sleep(5)
# AT command to hang up the call
hangup_command = b'ATH\r'
sock.send(hangup_command)
# Close the Bluetooth socket
sock.close()
print("Call has been made and hung up.")