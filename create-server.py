import os
import subprocess
from get_paper import get_latest_jar_url

# server adında bir klasör oluştur ve o klasöre git    
os.makedirs("server", exist_ok=True)
os.chdir("server")

# get-paper.py dosyasındaki latest_jar_url değişkeninden URL al
latest_jar_url = get_latest_paper_url()

# URL'den jar dosyasının adını ayıkla
jar_file_name = latest_jar_url.split('/')[-1]

# paper jar dosyasını wget ile indir
subprocess.run(["wget", latest_jar_url])

# Minimum ve maksimum RAM miktarını seç
min_ram = input("Minimum RAM miktarını girin (örn. 2G): ").strip()
max_ram = input("Maksimum RAM miktarını girin (örn. 4G): ").strip()

# start.sh dosyasını oluştur ve gerekli komutu ekle
with open("start.sh", "w") as file:
    file.write("#!/bin/sh\n")
    file.write(f"java -Xms{min_ram} -Xmx{max_ram} -XX:+UseG1GC -jar {jar_file_name} nogui\n")

# start.sh dosyasını çalıştırılabilir yap
subprocess.run(["chmod", "+x", "start.sh"])

# eula.txt dosyasını oluştur ve içeriği yaz
with open("eula.txt", "w") as file:
    file.write("eula=true\n")

# server.properties dosyasını oluştur, korsan durumu ve maksimum oyuncu sayısını sor
online_mode = input("Korsan aktif olsun mu? (evet/hayır): ").strip().lower()
max_players = input("Maksimum oyuncu sayısı kaç olsun?: ").strip()

with open("server.properties", "w") as file:
    if online_mode == "evet":
        file.write("online-mode=false\n")
    else:
        file.write("online-mode=true\n")
    file.write(f"max-players={max_players}\n")

# Sunucu açıklaması ne olsun diye sor ve server.properties dosyasına ekle
motd = input("Sunucu açıklaması ne olsun?: ").strip()
with open("server.properties", "a") as file:
    file.write(f"motd={motd}\n")

# start.sh dosyasını çalıştır
subprocess.run(["./start.sh"])
