from sqlalchemy import Integer, String, Float, Column
from db.db_setup import Base


class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    month = Column(String(2))
    day_of_month = Column(String(2))
    year = Column(Integer)
    five_year_avg_temp = Column(Float)
    five_year_min_temp = Column(Float)
    five_year_max_temp = Column(Float)
    five_year_avg_wind_speed = Column(Float)
    five_year_min_wind_speed = Column(Float)
    five_year_max_wind_speed = Column(Float)
    five_year_sum_precipitation = Column(Float)
    five_year_min_precipitation = Column(Float)
    five_year_max_precipitation = Column(Float)

    def __init__(self, latitude, longitude, month, day_of_month, year, five_year_avg_temp, five_year_min_temp,
                 five_year_max_temp, five_year_avg_wind_speed, five_year_min_wind_speed, five_year_max_wind_speed,
                 five_year_sum_precipitation, five_year_min_precipitation, five_year_max_precipitation):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day_of_month = day_of_month
        self.year = year
        self.five_year_avg_temp = five_year_avg_temp
        self.five_year_min_temp = five_year_min_temp
        self.five_year_max_temp = five_year_max_temp
        self.five_year_avg_wind_speed = five_year_avg_wind_speed
        self.five_year_min_wind_speed = five_year_min_wind_speed
        self.five_year_max_wind_speed = five_year_max_wind_speed
        self.five_year_sum_precipitation = five_year_sum_precipitation
        self.five_year_min_precipitation = five_year_min_precipitation
        self.five_year_max_precipitation = five_year_max_precipitation

    # Format queries in command line
    def __repr__(self):
        return (f"\n**Last 5 years of weather data for:**\n"
                f"Primary key: {self.id}\n"
                f"LATITUDE: {self.latitude}\n"
                f"LONGITUDE: {self.longitude}\n"
                f"DATE (yyyy-mm-dd): {self.year}-{self.month}-{self.day_of_month}\n\n"
                f"TEMPERATURE DATA:\n"
                f"Average: {self.five_year_avg_temp} deg F\n"
                f"Minimum: {self.five_year_min_temp} deg F\n"
                f"Maximum: {self.five_year_max_temp} deg F\n\n"
                f"WIND SPEED DATA:\n"
                f"Average: {self.five_year_avg_wind_speed} mph\n"
                f"Minimum: {self.five_year_min_wind_speed} mph\n"
                f"Maximum: {self.five_year_max_wind_speed} mph\n\n"
                f"PRECIPITATION DATA:\n"
                f"Sum: {self.five_year_sum_precipitation} inches\n"
                f"Minimum: {self.five_year_min_precipitation} inches\n"
                f"Maximum: {self.five_year_max_precipitation} inches\n"
                )
