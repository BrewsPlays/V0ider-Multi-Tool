import os
import platform
import socket
import datetime
import requests
import psutil
from colorama import Fore
from pyfiglet import Figlet

def ping_ip(ip_address):
    """
    Pings the given IP address 50 times and returns the result.
    """
    print(Fore.GREEN + Figlet(font='slant').renderText('IP PINGER'))
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '50', ip_address]

    return os.system(' '.join(command)) == 0

def get_ip_address():
    """
    Gets and prints the IP address of the computer.
    """
    print(Fore.GREEN + Figlet(font='slant').renderText('GET IP ADDRESS'))
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"The IP address of your computer is {ip_address}")

def get_website_ip(website_url):
    """
    Gets and prints the IP address of a website.
    """
    print(Fore.GREEN + Figlet(font='slant').renderText('GET WEBSITE IP'))
    ip_address = socket.gethostbyname(website_url)
    print(f"The IP address of the website {website_url} is {ip_address}")

def get_ip_location(ip_address):
    """
    Gets and prints the location of an IP address.
    """
    print(Fore.GREEN + Figlet(font='slant').renderText('GET IP LOCATION'))
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    location_info = response.json()
    print(f"The location of the IP address {ip_address} is {location_info['city']}, {location_info['region']}, {location_info['country']}")

def print_current_time():
    """
    Prints the current time and date.
    """
    print(Fore.GREEN + Figlet(font='slant').renderText('CURRENT TIME'))
    now = datetime.datetime.now()
    print(f"The current time and date is {now}")

def print_system_info():
    """
    Prints information about the system.
    """
    print(Fore.GREEN + Figlet(font='slant').renderText('SYSTEM INFO'))
    print(f"System name: {platform.system()}")
    print(f"System version: {platform.release()}")
    print(f"System architecture: {platform.architecture()[0]}")

def print_system_performance():
    """
    Prints information about the system performance.
    """
    print(Fore.GREEN + Figlet(font='slant').renderText('SYSTEM PERFORMANCE'))
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    print(f"CPU usage: {cpu_usage}%")
    print(f"Memory usage: {memory_usage}%")
    print(f"Disk usage: {disk_usage}%")

def main():
    while True:
        print(Fore.BLUE + Figlet(font='slant').renderText("V0ider Multi-tool"))
        print("1. Ping IP")
        print("2. Get IP address")
        print("3. Get website IP")
        print("4. Get IP location")
        print("5. Print current time and date")
        print("6. Print system info")
        print("7. Print system performance")
        print("8. Exit program")
        choice = input("Enter your choice: ")

        if choice == '1':
            ip_address = input("Enter IP address to ping: ")
            if ping_ip(ip_address):
                print(Fore.GREEN + f"IP address {ip_address} is available.")
            else:
                print(Fore.RED + f"IP address {ip_address} is not available.")
        elif choice == '2':
            get_ip_address()
        elif choice == '3':
            website_url = input("Enter website URL: ")
            get_website_ip(website_url)
        elif choice == '4':
            ip_address = input("Enter IP address to get location: ")
            get_ip_location(ip_address)
        elif choice == '5':
            print_current_time()
        elif choice == '6':
            print_system_info()
        elif choice == '7':
            print_system_performance()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
