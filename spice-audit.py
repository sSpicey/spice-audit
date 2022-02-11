import socket
from art import text2art
import os
from termcolor import colored

os.system('cls')


def print_logo():
    Art = colored(text2art("SPICE  LOCKPICK"), 'red')
    print(Art)


def scan(target, ports):
    print('\n' + ' Starting Scan For ' + str(target))
    for port in range(1, ports):
        scan_port(target, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(colored("[+] Port Opened ", 'green') + str(port))
        sock.close()
    except:
        pass


print_logo()
targets = input(colored("[*] Enter Targets To Scan(split them by ,): ", 'red'))
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
    print(colored(("[*] Scanning Multiple Targets"), 'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)
