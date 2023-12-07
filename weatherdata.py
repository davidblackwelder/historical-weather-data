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