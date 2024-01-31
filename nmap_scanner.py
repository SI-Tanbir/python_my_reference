import nmap

scanner=nmap.PortScanner()
print("Welcome to NMAP PORT scanner")

print("<------------------------------------------->")

ip_addr=input("please enter the IP address you want to scan:-")

print(f"The IP address is : {ip_addr}")

type(ip_addr)
 
req=input("""\n  Please enter the the type of scan you want to perform
1.SYN ACK scan
2.UDP Scan
3.Comprehensive scan \n :-  """)

print(f"you have selected option: {req}")

if req =="1":
     print("Nmap version:",scanner.nmap_version())

     scanner.scan(ip_addr,'1-1024','-v3 -sS')
     print(scanner.scaninfo())
     print("IP status:",scanner[ip_addr].state())
     print(scanner[ip_addr].all_protocols())
     print("Open Port:",scanner[ip_addr]['tcp'].keys())
elif req =="2":
    print("Nmap version:",scanner.nmap_version())
    scanner.scan(ip_addr,'1-1024','-v -sU')
    print(scanner.scaninfo())
    print("IP status:",scanner[ip_addr].state())

    print(scanner[ip_addr].all_protocols())

    print("Open Port:",scanner[ip_addr]['udp'].keys())

elif req == "3":
    print("Nmap version:",scanner.nmap_version())
    scanner.scan(ip_addr,'1-1024','-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP status:",scanner[ip_addr].state())

    print(scanner[ip_addr].all_protocols())

    print("Open Port:",scanner[ip_addr]['tcp'].keys())

    
elif req >="4":
    print("Invalid input")
