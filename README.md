
#Weather Data App

This is a simple web application that displays weather data for Kingston, Jamaica. The application uses the Stormglass API to retrieve data on air temperature, pressure, and precipitation. The data is then displayed in real-time on a web page using Flask and Jinja templates. The application also includes a CSS file to style the page and make it look more presentable.

Installation

To run this application, you'll need Python 3.x and the Flask library installed on your machine. You can install Flask using pip:

sh
Copy code
pip install Flask
Once Flask is installed, you can run the app using the following command:

sh
Copy code
python app.py
This will start the Flask development server and the app will be accessible at http://localhost:5000.

Usage

Once the app is running, you can open your web browser and navigate to http://localhost:5000 to view the weather data for Kingston, Jamaica.

The app displays the following weather data:

Timestamp (Jamaica time)
Air temperature (°C)
Air pressure (hPa)
Precipitation (kg/m²/h = mm/h)
The data is updated in real-time and reflects the current weather conditions in Kingston, Jamaica.

Customization

This project can be customized to display weather data for any location that is supported by the Stormglass API. To change the location, simply update the latitude and longitude values in the params dictionary in the app.py file:

python
Copy code
params={
    'lat': 17.9926,  # Latitude of the location
    'lng': -76.7920,  # Longitude of the location
    'params': ','.join(['airTemperature', 'pressure', 'precipitation']),
    'start': start.to('UTC').timestamp(),
    'end': end.to('UTC').timestamp()
}
You can also customize the app's appearance by modifying the CSS file (static/style.css).


