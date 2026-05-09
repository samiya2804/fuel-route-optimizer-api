from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from routing.serializers import RouteRequestSerializer
from routing.services.route_service import RouteService
from routing.services.optimizer import FuelOptimizer

class TestAPIView(APIView):

    def get(self, request):
        return Response({
            "message": "Fuel Optimizer API Working"
        })
    
class RouteOptimizationView(APIView):

    def post(self, request):

        serializer = RouteRequestSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        start = serializer.validated_data['start']
        destination = serializer.validated_data['destination']

        route_data = RouteService.get_route(start, destination)

        optimizer = FuelOptimizer(route_data)
        fuel_stops = optimizer.recommend_stops()

        total_cost = optimizer.estimate_total_cost()

        response = {
            'start': start,
            'destination': destination,
            'distance_miles': round(route_data['distance_miles'], 2),
            'fuel_stops': fuel_stops,
            'estimated_total_fuel_cost': total_cost,
            'route_geometry': route_data['geometry']
        }

        return Response(response, status=status.HTTP_200_OK)
