import traceback
from nOBEX.common import OBEXError
from clients.opp import OPPClient
import sys

def send_file_via_opp(mac_address, file_name):
    try:
        c = OPPClient(mac_address)
        c.connect()
    except OBEXError:
        sys.stderr.write("Failed to connect.\n")
        traceback.print_exc()
        return False

    try:
        c.put(file_name, open(file_name, 'rb').read())
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        c.disconnect()

if __name__ == "__main__":
    mac_address = input("Enter MAC address: ")
    file_name = input("Enter file name: ")

    success = send_file_via_opp(mac_address, file_name)

    if success:
        print("File sent successfully via OPP.")
    else:
        print("Failed to send file via OPP.")
