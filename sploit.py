import os

import time

import socket

import sys

import ipaddress

import requests

import platform

from colorama import Fore, Style
print(Fore.RED + "")

os.system("figlet sploiter")
      


system_info = {}

system_info['İşletim Sistemi'] = platform.system()

system_info['Sürüm'] = platform.release()

system_info['Mimarisi'] = platform.machine()

for category, info in system_info.items():

    print(category)

    print('=' * 30)

    print(info)

    print() 




print(Style.RESET_ALL)

print(Fore.YELLOW +  """

      [ CODED BY ENESXSEC ]

        insta: enesxsec""")

os.system("neofetch --ascii_distro blackarch")

def yukleme_animasyonu():

    animasyon_karakterleri = ["|", "/", "-", "\\"]

    for i in range(10):

        animasyon = f"Yükleniyor... {animasyon_karakterleri[i % len(animasyon_karakterleri)]}"

        sys.stdout.write(animasyon)

        sys.stdout.flush()

        time.sleep(0.1)

        sys.stdout.write("\b" * len(animasyon))

        sys.stdout.flush()

yukleme_animasyonu()

print("Tamamlandı!")

def get_local_ip():

    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.connect(("8.8.8.8", 80))

        local_ip = sock.getsockname()[0]

        sock.close()

        return local_ip

    except socket.error:

        return "IP adresi alınamadı."

ip_address = get_local_ip()

print("Yerel IP Adresiniz:", ip_address)

hostname = socket.gethostname()

print("Hostname:", hostname)

response = requests.get("http://ip-api.com/json")

data = response.json()

gateway = data["query"]

print("Ağ Geçidi:", gateway)

time.sleep(2)

print(Fore.RED + """--------------------------------------""")

print("> 1. ve 2. MADDELER NMAP TARAMASI İÇİNDİR")

time.sleep(1)

print(Fore.BLUE + """

[1] NMAP SCANNER

[2] NMAP PING SCANNER

[3] E-VİRÜS

[4] SUBNET SCANNER

""")

print(Style.RESET_ALL)

print(Fore.RED + "--------------------------------------")

islemno=input("İşlem numarası giriniz: ")

if islemno=="1":

        hedefip=input("hedef HOST giriniz : ")

        os.system("nmap -sT -v "+hedefip)

if islemno=="2":

        hedefip=input("hedef HOST giriniz : ")

        os.system("nmap -sP -v  "+hedefip)

if islemno=="3":

        hedefip=input("VİRÜSLÜ LİNKİ ALMAK İÇİN ENTER BAS: ")

        time.sleep(2)

        print(Fore.YELLOW + "> https://tinyurl.com/uppdatesnew <")

if islemno=="4":

    ip_adresi = input("IP adresini girin (örneğin, 192.168.0.0): ")

    prefix = int(input("Prefix uzunluğunu girin (örneğin, 24): "))

    network = ipaddress.ip_network(ip_adresi + '/' + str(prefix), strict=False)

    subnetler = list(network.subnets(new_prefix=prefix))

    print(f"\nAna ağ: {network.network_address}/{network.prefixlen}")

    print(f"Alt ağ sayısı: {len(subnetler)}\n")

    for subnet in subnetler:

        print(subnet)

islemno = input("LÜTFEN 1 SAYISINA TIKLAYINIZ:  ")

print("--------------------------------------")

islemno=input("wordlist aracına gitmek için enter bas yada çıkmak için CTRL+C yap: ")

os.system("figlet wordlist")

def cupp():

    print(Fore.YELLOW + """

[1] WORDLİST OLUŞTURMA ARACINI YÜKLE

[2] WORDLİST OLUŞTURMA

[0] IP TARA

⟩ SİTE İP TARAMAK İSTİYORSANIZ 0 SAYISINA BASIN

""")

    islemno=input("secim: ")

    if islemno=="1":

        os.system("clear")

        os.system("git clone https://github.com/Mebus/cupp.git")

        print("Arac yüklenmiştir")

        time.sleep(2)

        os.system("clear")

        cupp()

    elif islemno=="2":

        os.system("clear")

        os.system("python3 ./cupp/cupp.py -i")

        os.system("clear")

        cupp()

    elif islemno=="0":

        os.system("")

        anapg()

    else:

        print("yanlış tuşlama")

        time.sleep(2)

        cupp()

def anapg():

    pass

cupp()

print(">>>>>Biraz bekleyin site ip tarama aracına yönlendiriliyorsunuz<<<<<")

time.sleep(4)

os.system("figlet IP")

def check_ip_address(domain):

    try:

        ip = socket.gethostbyname(domain)

        print("Site: {}  IP Adresi: {}".format(domain, ip))

    except socket.gaierror:

        print("Geçersiz bir site adı.")

site = input("Site girin: ")

check_ip_address(site)

def get_local_ip():

    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.connect(("8.8.8.8", 80))

        local_ip = sock.getsockname()[0]

        sock.close()

        return local_ip

    except socket.error:

        return "IP adresi alınamadı."

ip_address = get_local_ip()

print("Kendi Yerel IP Adresiniz:", ip_address)

hostname = socket.gethostname()

print("Hostname:", hostname)

response = requests.get("http://ip-api.com/json")

data = response.json()

gateway = data["query"]

print("Ağ Geçidiniz:", gateway)
