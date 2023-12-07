from weatherdata import WeatherData
from db.db_setup import engine, session_local
from db.models import weather
from db.models.weather import Weather

# set user-defined information
# this could be interactive but for now it will be hard-coded for proof of concept
latitude = 35.487167
longitude = -80.858528
month = "07"
day_of_month = "18"
# year should be only one year in the future since API can only pull historical data
year = 2024
years = []
dates = []
avg_temps = []
max_temps = []
min_temps = []
wind_speeds = []
precipitation_sums = []

# set BASE and END API url info, more info on API can be found here https://open-meteo.com/en/docs
BASE_URL = "https://archive-api.open-meteo.com/v1/archive?"

# Get max, min, and mean temps in Fahrenheit
# Get precipitation sum in inches
# Get wind speeds in mph
END_URL = "daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,precipitation_sum,wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York"

# Create an instance of the WeatherData() class from weatherdata.py
w = WeatherData(latitude, longitude, month, day_of_month, year)

# Using the determine_historical_dates method to determine the start and end dates to use with the API call
# Stores the dates in a string format to be used in the FINAL_URL when making a GET request
dates = w.determine_historical_dates(year, month, day_of_month, years, dates)

for date in dates:
    start_date = date # "YYYY-MM-DD"
    end_date = date # "YYYY-MM-DD"
    # makes one API call per start/end date and stores response
    weatherdata_response = w.get_weatherdata_response(
        start_date, end_date, BASE_URL, END_URL)
    # get each avg_temp response to store in an array
    avg_temps = w.get_mean_temps(weatherdata_response, avg_temps)
    # get each min_temp response to store in an array
    min_temps = w.get_min_temps(weatherdata_response, min_temps)
    # get each max_temp response to store in an array
    max_temps = w.get_max_temps(weatherdata_response, max_temps)
    # get each max_wind_speeds response to store in an array
    wind_speeds = w.get_max_wind_speeds(
        weatherdata_response, wind_speeds)
    # get each precipitation_sum response to store in an array
    precipitation_sums = w.get_precipitation_sum(
        weatherdata_response, precipitation_sums)

# Use avg_temps array from loop above to calculate each temp attribute
w.five_year_avg_temp = w.calc_5_year_avg_temp(avg_temps)
w.five_year_min_temp = w.calc_5_year_min_temp(avg_temps)
w.five_year_max_temp = w.calc_5_year_max_temp(avg_temps)

# Use max_wind_speeds array from loop above to calculate each wind attribute
w.five_year_avg_wind_speed = w.calc_5_year_avg_wind_speed(wind_speeds)
w.five_year_min_wind_speed = w.calc_5_year_min_wind_speed(wind_speeds)
w.five_year_max_wind_speed = w.calc_5_year_max_wind_speed(wind_speeds)

# Use sum_precipitation array from loop above to calculate each precipitation attribute
w.five_year_sum_precipitation = w.calc_5_year_precipitation_sum(
    precipitation_sums)
w.five_year_min_precipitation = w.calc_5_year_min_precipitation_sum(
    precipitation_sums)
w.five_year_max_precipitation = w.calc_5_year_max_precipitation_sum(
    precipitation_sums)

# Create schema for weather Table from db_setup.py
weather.Base.metadata.create_all(bind=engine)

# Create a model instance of Weather() using attributes from the WeatherData() instance
weather = Weather(w.latitude, w.longitude, w.month, w.day_of_month,
                  w.year, w.five_year_avg_temp, w.five_year_min_temp,
                  w.five_year_max_temp, w.five_year_avg_wind_speed, w.five_year_min_wind_speed,
                  w.five_year_max_wind_speed, w.five_year_sum_precipitation, w.five_year_min_precipitation,
                  w.five_year_max_precipitation)

# Establish ability to connect with database from db_setup.py
# more details about Session can be found here:
# https://docs.sqlalchemy.org/en/20/orm/session_basics.html#what-does-the-session-do
with session_local as session:
    session.begin()
    try:
        session.add(weather)
    except:
        session.rollback()
        raise
    else:
        session.commit()

# Query table to retrieve data stored
results = session.query(Weather).all()

# Results will be formatted by __repr___ method for Weather() model class in weather.py
print(results)