import os
import subprocess
from get-paper import get_latest_paper_url

# server adında bir klasör oluştur ve o klasöre git
os.makedirs("server", exist_ok=True)
os.chdir("server")

# get-paper.py dosyasındaki latest_jar_url değişkeninden URL al
latest_jar_url = get_latest_paper_url()

# paper jar dosyasını wget ile indir
subprocess.run(["wget", latest_jar_url])

# start.sh dosyasını oluştur ve gerekli komutu ekle
with open("start.sh", "w") as file:
    file.write("#!/bin/sh\n")
    file.write("java -Xms4G -Xmx4G -XX:+UseG1GC -jar paper-1.21.1-122.jar nogui\n")

# start.sh dosyasını çalıştırılabilir yap
subprocess.run(["chmod", "+x", "start.sh"])

# eula.txt dosyasını oluştur ve içeriği yaz
with open("eula.txt", "w") as file:
    file.write("eula=true\n")

# server.properties dosyasını oluştur ve korsan aktif olsun mu diye sor
online_mode = input("Korsan aktif olsun mu? (evet/hayır): ").strip().lower()
with open("server.properties", "w") as file:
    if online_mode == "evet":
        file.write("online-mode=false\n")
    else:
        file.write("online-mode=true\n")

# Sunucu açıklaması ne olsun diye sor ve server.properties dosyasına ekle
motd = input("Sunucu açıklaması ne olsun?: ").strip()
with open("server.properties", "a") as file:
    file.write(f"motd={motd}\n")

# start.sh dosyasını çalıştır
subprocess.run(["./start.sh"])
