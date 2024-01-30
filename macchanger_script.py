import re
import subprocess
from random import choice,randint
import netifaces

def main():
    print("Enter 1 for manual changing of mac address and 2 for random mac address")
    inp=input()

    interfaces = netifaces.interfaces()
    for i, interface in enumerate(interfaces):
        print(f"{i}: {interface}")

    interface_index = int(input("Enter the number corresponding to your interface: "))
    interface = interfaces[interface_index]


# rest of your code

    if inp=="1":
        mac_name=input("Enter the new Mac Address: ").strip()
        new_mac(interface,mac_name)

    elif inp =="2":
        random_mac = mac_random()
        print(random_mac) 
        new_mac(interface,random_mac)

def mac_random():
    cisco=["00","40","96"]
    dell=["00","14","22"]
    mac_address=  choice([cisco,dell])
    
    for i in range(3):
        one= choice(str(randint(0,9)))
        two= choice(str(randint(0,9)))
        three=(str(one+two))
        mac_address.append(three)
        
    return ":".join(mac_address)

def new_mac(interface, new_mac_address):
    subprocess.call(["ifconfig "+ interface + " down"],shell = True)
    subprocess.call(["ifconfig "+ interface+ " hw ether " + new_mac_address],shell = True)
    subprocess.call(["ifconfig "+interface + " up"],shell = True)
    changed_mac=subprocess.check_output(["ifconfig " + interface],shell = True)
    mac_adds = re.search(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})", str(changed_mac))
    print(f"New mac address  {mac_adds.group()}")

def current_mac(interface):
    try:
        output = subprocess.check_output(["ifconfig "+ interface],shell = True)
        mac_add = re.search(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})", str(output))
        if mac_add:
            print(f" Old MAC Address: {mac_add.group()}")
        else:
            print("No MAC Address found.")
    except FileNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
