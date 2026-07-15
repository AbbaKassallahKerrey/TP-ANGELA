"""import requests

response = requests.get("https://www.google.com")
print(response.status_code)
"""
import requests
from datetime import datetime
import time

MY_LAT = 51.507351  
MY_LONG = -0.127758  


def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within ±5 degrees of the ISS position.
    return (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    )


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json",
        params=parameters
    )
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.utcnow().hour  # Les heures de l'API sont en UTC

    return time_now >= sunset or time_now <= sunrise


while True:
    time.sleep(60)

    if is_iss_overhead() and is_night():
        print("🌌 Look Up! The ISS is above you in the sky.")