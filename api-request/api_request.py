import requests

API_KEY = "eec21c4c8c5ead51f04def4152c69d6d"
api_url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query=New York"

# def fetch_data():
#     print("Fetching data from Weatherstack API...")
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()  # Raise an error for bad responses
#         print("API Response received successfully:")
#         return response.json()

#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")
#         raise

# fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-10-14 14:56', 'localtime_epoch': 1760453760, 'utc_offset': '-4.0'}, 'current': {'observation_time': '06:56 PM', 'temperature': 16, 'weather_code': 122, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'], 'weather_descriptions': ['Overcast'], 'astro': {'sunrise': '07:07 AM', 'sunset': '06:17 PM', 'moonrise': 'No moonrise', 'moonset': '03:17 PM', 'moon_phase': 'Waning Crescent', 'moon_illumination': 47}, 'air_quality': {'co': '237.85', 'no2': '26.95', 'o3': '50', 'so2': '5.55', 'pm2_5': '7.05', 'pm10': '7.45', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 23, 'wind_degree': 18, 'wind_dir': 'NNE', 'pressure': 1017, 'precip': 0, 'humidity': 72, 'cloudcover': 100, 'feelslike': 16, 'uv_index': 2, 'visibility': 16, 'is_day': 'yes'}}