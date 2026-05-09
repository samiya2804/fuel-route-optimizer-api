from geopy.distance import geodesic
from routing.services.fuel_service import FuelService


class FuelOptimizer:

    MAX_RANGE_MILES = 500
    MPG = 10

    def __init__(self, route_data):
        self.route_data = route_data
        self.fuel_service = FuelService()

    def estimate_total_cost(self):

        total_distance = self.route_data['distance_miles']

        gallons_needed = total_distance / self.MPG

        stations = self.fuel_service.get_all_stations()
        average_price = stations['Retail Price'].mean()

        total_cost = gallons_needed * average_price

        return round(total_cost, 2)

    def recommend_stops(self):

        total_distance = self.route_data['distance_miles']

        stations = self.fuel_service.get_all_stations()

        cheapest = stations.sort_values('Retail Price').head(5)

        recommendations = []

        stop_count = int(total_distance // self.MAX_RANGE_MILES)

        for i in range(stop_count):

            station = cheapest.iloc[i % len(cheapest)]

            recommendations.append({
                'truckstop_name': station['Truckstop Name'],
                'city': station['City'],
                'state': station['State'],
                'retail_price': station['Retail Price']
            })

        return recommendations