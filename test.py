import unittest
from weatherdata import WeatherData

class TestWeatherData(unittest.TestCase):
    # Create test WeatherData() instance
    def setUp(self):
        self.wd = WeatherData(35.487167, -80.858528, "12", "29", 2024)

    # Test the temperature data functions for avg, min, and max
    def test_calc_5_year_avg_temp(self):
        avg_temps = [-10, 20, -30, 40, 50]
        self.assertEqual(self.wd.calc_5_year_avg_temp(avg_temps), round(sum(avg_temps)/len(avg_temps)))

    def test_calc_5_year_min_temp(self):
        avg_temps = [-10, 20, -30, 40, 50]
        self.assertEqual(self.wd.calc_5_year_min_temp(avg_temps), min(avg_temps))

    def test_calc_5_year_max_temp(self):
        avg_temps = [-10, 20, -30, 40, 50]
        self.assertEqual(self.wd.calc_5_year_max_temp(avg_temps), max(avg_temps))

    # Test the wind speed data functions for avg, min, and max
    def test_calc_5_year_avg_wind_speed(self):
        wind_speeds = [10.6, 4.8, 7.5, 20.4, 1.5]
        self.assertEqual(self.wd.calc_5_year_avg_wind_speed(wind_speeds), round(sum(wind_speeds)/len(wind_speeds)))

    def test_calc_5_year_min_wind_speed(self):
        wind_speeds = [10.6, 4.8, 7.5, 20.4, 1.5]
        self.assertEqual(self.wd.calc_5_year_min_wind_speed(wind_speeds), min(wind_speeds))

    def test_calc_5_year_max_wind_speed(self):
        wind_speeds = [10.6, 4.8, 7.5, 20.4, 1.5]
        self.assertEqual(self.wd.calc_5_year_max_wind_speed(wind_speeds), max(wind_speeds))

    # Test the sum precipitation data functions for sum, min, and max
    def test_calc_5_year_precipitation_sum(self):
        sum_precipitation = [0.003, 0.0385, 0.000, 0.156, 1.368]
        self.assertEqual(self.wd.calc_5_year_precipitation_sum(sum_precipitation), sum(sum_precipitation))

    def test_calc_5_year_min_precipitation_sum(self):
        sum_precipitation = [0.003, 0.0385, 0.000, 0.156, 1.368]
        self.assertEqual(self.wd.calc_5_year_min_precipitation_sum(sum_precipitation), min(sum_precipitation))

    def test_calc_5_year_max_precipitation_sum(self):
        sum_precipitation = [0.003, 0.0385, 0.000, 0.156, 1.368]
        self.assertEqual(self.wd.calc_5_year_max_precipitation_sum(sum_precipitation), max(sum_precipitation))

if __name__ == '__main__':
    unittest.main()