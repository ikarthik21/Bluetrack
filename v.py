import pySim

def read_sms(mac_address, port):
    client_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    client_sock.connect((mac_address, port))

    sim = pySim.SIM(client_sock)

    sms_messages = sim.read_sms()

    for message in sms_messages:
        print("Sender: " + message.sender)
        print("Message: " + message.text)

    client_sock.close()


if __name__ == "__main__":
    mac_address = input("Enter MAC address: ")
    port = 6

    read_sms(mac_address, port)