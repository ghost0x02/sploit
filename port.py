import os

os.system("figlet root nmap")

os.system("apt install python3 -y")

os.system("apt install figlet -y")

os.system("apt install nmap -y")

import os

os.system("figlet root")

os.system("figlet nmap 1 . 2")

print("Dikkat 5. ve 6. maddeler icin root kullanici olmaniz gerekir. ")
print("⟩coded by enesxsec ⟨")
print("""

1-) Hizli port tarayici

2-) Servis ve versiyon bulucu

3-) Nmap bilgi kitabi

4-) Ping taramasi

5-) ip protokolu taramasi

6-) Bosta tarama yontemi

""")

islemno=input("islem numarasi giriniz :")

if islemno=="1":

        hedefip=input("hedef ip giriniz : ")

        os.system("nmap "+hedefip)

elif islemno=="2":

        hedefip=input("hedef ip giriniz : ")

        os.system("nmap -sS -sV "+hedefip)

elif islemno=="3":

        hedefip=input("nmap hakkinda bilgi almak icin enter bas :")

        os.system("nmap -h "+hedefip)

elif islemno=="4":

        hedefip=input("hedef ip giriniz : ")

        os.system("nmap -sP -v  "+hedefip)

elif islemno=="5":

        hedefip=input("Hedef ip giriniz : ")

        os.system("nmap -sO -v "+hedefip)

elif islemno=="6":

        hedefip=input("Hedef ip giriniz : ")

        os.system("nmap -sI -v "+hedefip)

else:

        print("yanlis tusa bastiniz")
