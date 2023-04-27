from flask import Flask, render_template
import arrow
import requests
import datetime

app = Flask(__name__)

# Set the timezone for Jamaica
tz = 'America/Jamaica'

@app.route("/")
def index():
    # Get the current time in Jamaica
    now = arrow.now(tz)

    # Set the start time to the beginning of the current hour in Jamaica
    start = now.floor('hour')

    # Set the end time to the end of the current hour in Jamaica
    end = now.ceil('hour')

    response = requests.get(
      'https://api.stormglass.io/v2/weather/point',
      params={
        'lat': 17.9926,  # Kingston, Jamaica latitude
        'lng': -76.7920,  # Kingston, Jamaica longitude
        'params': ','.join(['airTemperature', 'pressure', 'precipitation']),
        'start': start.to('UTC').timestamp(),  # Convert to UTC timestamp
        'end': end.to('UTC').timestamp()  # Convert to UTC timestamp
      },
      headers={
        'Authorization': '58a64b7c-e514-11ed-86b2-0242ac130002-58a64c30-e514-11ed-86b2-0242ac130002'
      }
    )

    # Do something with response data.
    json_data = response.json()
    weather_data = json_data['hours'][0]

    # Get the current time in the user's timezone
    now_local = datetime.datetime.now()

    # Convert timestamp to Jamaica time
    timestamp = arrow.get(weather_data['time']).to(tz).strftime("%Y-%m-%d %H:%M:%S")

    # Render the template with the data
    return render_template("index.html", timestamp=timestamp, temperature=weather_data['airTemperature']['noaa'], pressure=weather_data['pressure']['noaa'], precipitation=weather_data['precipitation']['noaa'], current_time=now_local.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    app.run(debug=True)
