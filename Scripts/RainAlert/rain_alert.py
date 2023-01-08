import requests
import datetime as dt
from twilio.rest import Client

# Constants
API_ENDPOINT = "https://api.open-meteo.com/v1/forecast"
API_DOCS = "https://open-meteo.com/en/docs#api_form"
PARAMETERS = {
    "latitude": 46.91,
    "longitude": 19.69,
    "hourly": "precipitation"
}

TWILIO_ACC_SID = "ACacfd54ccaa982ab8251548c8f40650a0"
TWILIO_AUTH_TOKEN = "0975f63c35575996deab22ab5b88ac37"
TWILIO_PHONE_NUMBER = "+13856006090"

DATE_FORMAT = "20%y-%m-%d"
HOURS_CHECKED = ["0"+str(num) if num < 10 else str(num) for num in range(7, 17)]

TODAYS_DATE = dt.date.today()

# data
response = requests.get(API_ENDPOINT, params=PARAMETERS)
response.raise_for_status()

data = response.json()
data_time_weather = data["hourly"]

hourly_precipitation = {
    time: precipitation
    for time, precipitation in zip(data_time_weather["time"], data_time_weather["precipitation"])
}

will_rain = False
for time, precipitation in hourly_precipitation.items():
    if (
            time.partition("T")[0] == TODAYS_DATE.strftime(DATE_FORMAT) and
            time.partition("T")[2].partition(":")[0] in HOURS_CHECKED and
            precipitation > 0
    ):
        will_rain = True

if will_rain:
    print("Will rain")
    client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="Ma 7 oratol 16 oraig VALAMIKOR esni fog az eso.",
        from_=TWILIO_PHONE_NUMBER,
        to="+36302804337"
    )

else:
    print("Won't rain")
    client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="Ma 7 oratol 16 oraig NEM fog esni az eso.",
        from_=TWILIO_PHONE_NUMBER,
        to="+365134561"
    )
