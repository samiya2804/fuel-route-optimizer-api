import pandas as pd
from geopy.distance import geodesic


class FuelService:

    def __init__(self):
        self.df = pd.read_csv('data/fuel-prices-for-be-assessment.csv')

    def get_all_stations(self):
        return self.df