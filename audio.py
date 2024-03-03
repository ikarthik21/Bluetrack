import bluetooth

def stream_audio(mac_address, port):
    client_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    client_sock.connect((mac_address, port))

    a2dp = bluetooth.A2DP(client_sock)

    a2dp.connect()

    # Replace "audio_file.mp3" with the path to the audio file you want to stream
    with open("audio.mp3", "rb") as f:
        a2dp.send(f.read())

    a2dp.disconnect()
    client_sock.close()


if __name__ == "__main__":
    mac_address = input("Enter MAC address: ")
    port = 5

    stream_audio(mac_address, port)