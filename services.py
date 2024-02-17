import bluetooth

 

def get_services(mac_address):
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    
    device = None
    for addr, name in nearby_devices:
        if addr == mac_address:
            device = addr
            break

    if device is None:
        print(f"Device with MAC address {mac_address} not found.")
    else:
        print(f"Device found: {name} ({device})")

       
        services = bluetooth.find_service(address=device)

        for i, s in enumerate(services):
           
            print("\n\n\n")
            print(f"Service ({i}):")
            print(f"    Service Class ID List: {s['service-classes']}")
            print(f"    Name: {s['name']}")
            print(f"    Port: {s['port']}")
            print(f"    Protocol Descriptor List: {s['protocol']}")
            print(f"    Bluetooth profile: {s['profiles']}")
            print(f"    Service name: {s['name']}")
            print(f"    Service description: {s['description']}")
            print(f"    Service provider: {s['provider']}")
            print(f"    Service ID: {s['service-id']}")

 