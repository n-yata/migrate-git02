import requests

print("hello, welcome!")

def get_weather_open_meteo(lat=35.6895, lon=139.6917, timezone="Asia/Tokyo"):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&hourly=temperature_2m,precipitation"
        f"&timezone={timezone}"
    )
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    # 必要な情報を抽出
    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])
    precs = data.get("hourly", {}).get("precipitation", [])
    return list(zip(times, temps, precs))

if __name__ == "__main__":
    for t, temp, prec in get_weather_open_meteo():
        print(f"{t}: {temp}°C, 降水量 {prec} mm")
