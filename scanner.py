import os
import sys
import subprocess

def scan_for_printers():
    masscan_command = "masscan -p9100 --banners --randomize-hosts --rate=1000 -e tun0 0.0.0.0/0 | grep -oP '(?<=Discovered open port 9100/tcp on )[^ ]+'"
    result = os.popen(masscan_command).read()

    if result:
        print("The following IP addresses have open 9100/tcp ports, which may indicate vulnerable printers:")
        print(result)
    else:
        print("No vulnerable printers were found.")

def scan_for_eternal_blue():
    masscan_command = "masscan -p445 --banners --randomize-hosts --rate=1000 -e tun0 0.0.0.0/0 | grep -oP '(?<=Discovered open port 445/tcp on )[^ ]+'"
    result = os.popen(masscan_command).read()

    if result:
        print("The following IP addresses have open 445/tcp ports, which may indicate vulnerable hosts:")
        print(result)
    else:
        print("No vulnerable hosts were found.")

def scan_for_passwordless_ssh():
    masscan_command = "masscan -p22 --banners --randomize-hosts --rate=1000 -e tun0 0.0.0.0/0 | grep -oP '(?<=Discovered open port 22/tcp on )[^ ]+'"
    result = os.popen(masscan_command).read()

    if result:
        print("The following IP addresses have open 22/tcp ports, which may indicate passwordless SSH services:")
        print(result)
    else:
        print("No passwordless SSH services were found.")

def nmap_fingerprint(ip_address):
    nmap_command = "nmap -O --osscan-guess " + ip_address
    result = subprocess.run(nmap_command.split(), stdout=subprocess.PIPE)
    output = result.stdout.decode()

    print("Fingerprint results for " + ip_address + ":")
    print(output)

def nmap_subdomain_enum(domain_name):
    nmap_command = "nmap -sL --script dns-brute " + domain_name
    result = subprocess.run(nmap_command.split(), stdout=subprocess.PIPE)
    output = result.stdout.decode()

    print("Subdomain and IP address results for " + domain_name + ":")
    print(output)

def nmap_exif_spider(domain_name):
    nmap_command = "nmap --script http-exif-spider " + domain_name
    result = subprocess.run(nmap_command.split(), stdout=subprocess.PIPE)
    output = result.stdout.decode()

    print("Exif data results for " + domain_name + ":")
    print(output)

def print_help_menu():
    print("Select a scan option:")
    print("1. Scan for vulnerable printers")
    print("2. Scan for Eternal Blue")
    print("3. Scan for passwordless SSH services")
    print("4. Nmap fingerprint")
    print("5. Nmap subdomain enumeration")
    print("6. Nmap exif data spider")
    print("9. Quit")

def completed_scan():
    print("Sifting through the scan results... this may take a while.")
    with open("results.txt", "r") as f:
        open_systems = [line.split()[5] for line in f if "Discovered open port" in line]

    with open("open_systems.txt", "w") as f:
        f.write("\n".join(open_systems))

    print("Cleaning up the mess... just like mom used to do.")
    os.remove("results.txt")

    print("Ta-da! List of open systems found:")
    with open("open_systems.txt", "r") as f:
        print(f.read())

    print("That's all folks! Time to go catch some zzz's.")

print_help_menu()

choice = input("Enter your choice (1-6): ")

if choice == "1":
    scan_for_printers()
elif choice == "2":
    scan_for_eternal_blue()
elif choice == "3":
    scan_for_passwordless_ssh()
elif choice == "4":
    nmap_fingerprint(input("Enter a domain name: "))
elif choice == "5":
    nmap_subdomain_enum(input("Enter a domain name: "))
elif choice == "6":
    nmap_exif_spider(input("Enter a domain name: "))
elif choice == "9":
    print("Hope this helped. Good Bye.")
    sys.exit(1)
else:
    print("Invalid choice.")
    sys.exit(1)

completed_scan()