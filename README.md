# Historical Weather Data

### Description
This project is designed to help our event business
plan for events and procure suitable coverings for events
of different sizes, such as tents, canopies, and other temporary
shelters. Weather data for a chosen location and day will be collected
and stored in our database.

## Project Requirements
- Uses the [Open-Mateo Weather API](https://open-meteo.com/en/docs)
- Database is SQLite3
- Python version 3.12.0
- Use `pip install requests` to interact with the API
- Use `pip install sqlalchemy` to interact with the database using Python

## How To Use Project
- Download zip file from [Gitlab](https://gitlab.com/wgu-gitlab-environment/student-repos/dbla367/d493-scripting-and-programming-applications/-/tree/david-main?ref_type=heads)
- Unzip the files
- Update the variables for your location and date in the `main.py` file:
  - `latitude` should be a Float type
  - `longitude` should be a Float type
  - `month` should be a String type and written as two-digits. July would be "07"
  - `day_of_month` should be a String type and written as two-digits. First day of the month would be "01"
  - `year` should be an Integer type
- Run the command `python main.py` to run the program and store the data in the database.
  - You may need to specify the version of python to run such as `python3 main.py`
- You can run the unit tests by running the command `python test.py`


## What data is stored in the database?
- Each entry in the database has a primary key field that is autoincremmented
- The columns in the table include:
  - `id`, Integer, Primary Key
  - `latitude`, Float
  - `longitude`, Float
  - `month`, String(2)
  - `day_of_month`, String(2)
  - `year`, Integer
  - `five_year_avg_temp`, Float
  - `five_year_min_temp`, Float
  - `five_year_max_temp`, Float
  - `five_year_avg_wind_speed`, Float
  - `five_year_min_wind_speed`, Float
  - `five_year_max_wind_speed`, Float
  - `five_year_sum_precipitation`, Float
  - `five_year_min_precipitation`, Float
  - `five_year_max_precipitation`, Float