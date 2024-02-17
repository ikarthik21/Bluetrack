import bluetooth

def run_scan():
    print("\n")
    print("{:<23}  {}  {}".format("Device Name 💻", "📌 MAC Address", "     📶 Signal Strength" ))
    print("\n")
    bluetooth_devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)
    for device in bluetooth_devices:
        device_name = device[1]
        mac_address = device[0]

     
        signal_strength_str = device[1].split(" ")[-1]
        
        signal_strength_str = ''.join(filter(str.isdigit, signal_strength_str))
        signal_strength_int = int(signal_strength_str)

        distance = calculate_distance(signal_strength_int)

        print("{:<27}  {}  {}".format(device_name, mac_address, signal_strength_str,"    ", distance))

def calculate_distance(signal_strength):
     
    max_signal_strength = -11100
    max_distance = 1110

    distance = max_distance - (signal_strength / max_signal_strength) * max_distance

    return distance

if __name__ == "__main__":
    run_scan()