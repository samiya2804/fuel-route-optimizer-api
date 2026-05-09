from django.urls import path
from routing.views import RouteOptimizationView
from .views import TestAPIView
urlpatterns = [
    path('optimize-route/', RouteOptimizationView.as_view()),
    path('', TestAPIView.as_view()),
]