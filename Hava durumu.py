import requests

def hava_durumu_sehir(ankara, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&lang=tr&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"{sehir} için hava durumu:")
        print(f"Sıcaklık: {data['main']['temp']}°C")
        print(f"Hava: {data['weather'][0]['description']}")
        print(f"Nem: {data['main']['humidity']}%")
        print(f"Rüzgar: {data['wind']['speed']} m/s")
    else:
        print("Hava durumu verisi alınamadı. Şehri veya API anahtarını kontrol edin.")

# Kullanım
api_key = "BURAYA_API_ANAHTARINI_YAZ"
sehir = "Ankara"
hava_durumu_sehir(sehir, api_key)