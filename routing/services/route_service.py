import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('ORS_API_KEY')

BASE_URL = 'https://api.openrouteservice.org'


class RouteService:

    @staticmethod
    def geocode(location):
        url = f'{BASE_URL}/geocode/search'

        params = {
            'api_key': API_KEY,
            'text': location,
            'size': 1,
            'boundary.country': 'USA'
        }

        response = requests.get(url, params=params)
        data = response.json()

        coordinates = data['features'][0]['geometry']['coordinates']

        return coordinates

    @staticmethod
    def get_route(start, destination):

        start_coords = RouteService.geocode(start)
        end_coords = RouteService.geocode(destination)

        url = f'{BASE_URL}/v2/directions/driving-car/geojson'

        headers = {
            'Authorization': API_KEY,
            'Content-Type': 'application/json'
        }

        body = {
            'coordinates': [
                start_coords,
                end_coords
            ]
        }

        response = requests.post(url, json=body, headers=headers)

        data = response.json()

        feature = data['features'][0]

        geometry = feature['geometry']['coordinates']

        summary = feature['properties']['summary']

        distance_meters = summary['distance']
        duration_seconds = summary['duration']
        distance_miles = distance_meters * 0.000621371

        return {
            'geometry': geometry,
            'distance_miles': distance_miles,
            'duration_seconds': duration_seconds
        }