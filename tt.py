import sys
import time
from bluetooth import BluetoothSocket, BluetoothError

def keyboard_emulation(target_addr, key_list):
    try:
        # Create a Bluetooth socket
        socket = BluetoothSocket()

        # Connect to the target device
        socket.connect((target_addr, 23))

        # Send the provided key sequence to the target device
        for key in key_list:
            print(f"Emulating key: {key}")
            socket.send(key.encode())
            time.sleep(0.1)

        # Close the connection
        socket.close()

    except BluetoothError as e:
        print(f"Connection failed with error: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python bt_keyboard_emulation.py [target_addr] [key_list]")
        sys.exit(1)

    target_addr = sys.argv[1]
    key_list = sys.argv[2]

    keyboard_emulation(target_addr, key_list)
