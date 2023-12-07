import requests

class WeatherData:

    def __init__(self, latitude, longitude, month, day_of_month, year):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day_of_month = day_of_month
        self.year = year
        self.five_year_avg_temp = 0
        self.five_year_min_temp = 0
        self.five_year_max_temp = 0
        self.five_year_avg_wind_speed = 0
        self.five_year_min_wind_speed = 0
        self.five_year_max_wind_speed = 0
        self.five_year_precipitation_sum = 0
        self.five_year_min_precipitation = 0
        self.five_year_max_precipitation = 0

    # Calculate past 5 years and adds string formatted date to a dates array
    def determine_historical_dates(self, year, month, day, years, dates):
        latest_year = year - 4
        while year >= latest_year:
            year -= 1
            years.append(year)

        for year in years:
            date = f"{year}-{month}-{day}"
            dates.append(date)

        return dates

    # Uses Weather API web link to get mean temperatures from JSON format and stores in an arr
    def get_mean_temps(self, response, arr):
        mean_temp = response['daily']['temperature_2m_mean']
        arr.append(mean_temp[0])
        return arr

    # Uses Weather API web link to get min temperatures from JSON format and stores in an arr
    def get_min_temps(self, response, arr):
        min_temp = response['daily']['temperature_2m_min']
        arr.append(min_temp[0])
        return arr

    # Uses Weather API web link to get max temperatures from JSON format and stores in an arr
    def get_max_temps(self, response, arr):
        max_temp = response['daily']['temperature_2m_max']
        arr.append(max_temp[0])
        return arr

    # Uses Weather API web link to get max wind speeds from JSON format and stores in an arr
    def get_max_wind_speeds(self, response, arr):
        max_wind_speeds = response['daily']['wind_speed_10m_max']
        arr.append(max_wind_speeds[0])
        return arr

    # Uses Weather API web link to get precipitation sum from JSON format and stores in an arr
    def get_precipitation_sum(self, response, arr):
        precipitation_sum = response['daily']['precipitation_sum']
        arr.append(precipitation_sum[0])
        return arr

    # Put together Weather API web link to get a response in JSON format to be used with
    # other functions
    def get_weatherdata_response(self, start_date, end_date, BASE_URL, END_URL):
        FINAL_URL = f"{BASE_URL}latitude={self.latitude}&longitude={
            self.longitude}&start_date={start_date}&end_date={end_date}&{END_URL}"

        response = requests.get(FINAL_URL).json()
        return response

    def calc_5_year_avg_temp(self, arr):
        avg_temp = sum(arr)/len(arr)
        return round(avg_temp, 1)

    def calc_5_year_min_temp(self, arr):
        min_temp = min(arr)
        return min_temp

    def calc_5_year_max_temp(self, arr):
        max_temp = max(arr)
        return max_temp

    def calc_5_year_avg_wind_speed(self, arr):
        avg_wind_speed = sum(arr)/len(arr)
        return round(avg_wind_speed, 1)

    def calc_5_year_min_wind_speed(self, arr):
        min_wind_speed = min(arr)
        return min_wind_speed

    def calc_5_year_max_wind_speed(self, arr):
        max_wind_speed = max(arr)
        return max_wind_speed

    def calc_5_year_precipitation_sum(self, arr):
        precipitation_sum = sum(arr)
        return precipitation_sum

    def calc_5_year_min_precipitation_sum(self, arr):
        min_precipitation_sum = min(arr)
        return min_precipitation_sum

    def calc_5_year_max_precipitation_sum(self, arr):
        max_precipitation_sum = max(arr)
        return max_precipitation_sum