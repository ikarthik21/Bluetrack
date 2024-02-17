with open("pins.txt", "w") as file:
    for i in range(1, 10000):
        pin = f"{i:04d}\n"
        file.write(pin)
