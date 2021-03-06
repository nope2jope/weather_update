import requests
import os
from twilio.rest import Client


#open weather map api request information
API_KEY = os.environ.get('OPEN_WEATHER_API')
LAT = os.environ.get('LATITUDE')
LON = os.environ.get('LONGITUDE')
EXCLUDE = 'current,minutely,daily'

#message to send given a rainy condition
UMBO = "Sniff, sniff. Anybody else smell cats and dogs? " \
       "That's right, looks like the Old Man Upstairs (praise be to unto Him) has a bit of a cat fancy after all! (Forecast says rain in the Seattle area. Stay saved.)"

#wi
AUTH = os.environ.get('AUTH_TOKEN')
ACC_SID = os.environ.get('ACC_SID_TOKEN')
NUM = os.environ.get('FROM_NUM')
NUM_TWO = os.environ.get('TO_NUM')

parameters = {
    'lat':LAT,
    'lon':LON,
    'appid':API_KEY,
    'exclude': EXCLUDE,

}

request = requests.get(url='http://api.openweathermap.org/data/2.5/onecall', params=parameters)
request.raise_for_status()

data = request.json()

rain_incoming = False

for entry in range(0, 12):
    x = (data['hourly'][entry]['weather'][0]['id'])
    if x < 700:
        rain_incoming = True

if rain_incoming:
    client = Client(ACC_SID, AUTH)

    message = client.messages \
        .create(
        body=UMBO,
        from_=NUM,
        to=NUM_TWO,
    )

    print(message.status)