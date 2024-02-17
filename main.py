import os
import time
from scan import run_scan   
from dos import run_dos   
from messages import extract_messages   
from phonebook import extract_phonebook  
from ftpclient import dump_ftp_directory  
from services import get_services
from push import send_file_via_opp

def main():
    print("\n\n 🚨 Welcome to Bluetrap by Team 41 🚨\n")
    while True:
        print("  \n💀 Select an option from below 💀\n")
        print("   1) 🔍 Scan")
        print("   2) 🎯 DOS")
        print("   3) 💬 Extract Messages")
        print("   4) 👥 Extract Contacts and call logs")
        print("   5) 🛠️ Services lookup")
        print("   6) 🗄️ Dump File")
        print("   7) 📁 Get Files from device")
        print("   8) 🔚 Exit")
    
        choice = input("\n Enter the action 🫡  :  ")

        if choice == "1":
            run_scan()  
        elif choice == "2":
            run_dos()  
        elif choice == "3":
            device_address = input("Enter the target device address (MAC): ")
            dest_dir = input("Enter the destination directory: ")
            extract_messages(device_address, dest_dir)  
        elif choice == "4":
            device_address = input("Enter the target device address (MAC): ")
            dest_dir = input("Enter the destination directory: ")
            extract_phonebook(device_address, dest_dir)   
        elif choice == "5":
            mac_address = input("Enter the MAC address of the device: ")
            get_services(mac_address)
        elif choice == "6":
            device_address = input("Enter the target device address (MAC): ")
            dest_dir = input("Enter the file path to send ")
            send_file_via_opp(device_address, dest_dir)  
        elif choice == "7":
            device_address = input("Enter the target device address (MAC): ")
            dest_dir = input("Enter the destination directory: ")
            dump_ftp_directory(device_address, dest_dir)  
        elif choice == "8":
            print("\n Exiting Bluetrap....")
            exit()
      
        else:
            print("Invalid choice. Please enter either ")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting Bluetrap....")
        exit()
    except Exception as e:
        print('[!] ERROR: ' + str(e))
