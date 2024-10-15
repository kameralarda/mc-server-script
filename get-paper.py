import requests

def get_latest_jar_url():
    url = "https://api.papermc.io/v2/projects/paper/versions/1.21.1/builds"
    response = requests.get(url)
    data = response.json()
    
    # Son build'i al
    latest_build = data["builds"][-1]
    build_number = latest_build["build"]
    
    # .jar dosyasının indirme linkini oluştur
    jar_url = f"https://api.papermc.io/v2/projects/paper/versions/1.21.1/builds/{build_number}/downloads/paper-1.21.1-{build_number}.jar"
    
    return jar_url

# Fonksiyonu çalıştır ve sonucu yazdır
latest_jar_url = get_latest_jar_url()
print("Son build'in .jar dosyasının indirme linki:", latest_jar_url)
