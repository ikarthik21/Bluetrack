import bluetooth
import time
import wave
 
def record_audio(mac_address, duration):
    service_matches = bluetooth.find_service(address=mac_address)
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((mac_address, 25))

    msg = "AT#VGS=15AT#ccat=1"
    sock.send(msg)
    time.sleep(1)

    # Create a new wave file
    wav_output = wave.open('output.wav', 'w')
    wav_output.setparams((1, 2, 8000, 0, 'NONE', 'not compressed'))

    start_time = time.time()
    # Read the audio data
    while time.time() - start_time < duration:
        data = sock.recv(1024)
        if len(data) == 0:
            break
        if data.startswith('#'):
            break
        wav_output.writeframes(data)

    wav_output.close()

mac_address = 'D4:8A:39:34:73:FD'  
duration = 10   
record_audio(mac_address, duration)