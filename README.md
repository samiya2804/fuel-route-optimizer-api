# Fuel Route Optimizer API

## Project Overview

Fuel Route Optimizer API is a Django REST API that calculates optimized road trip routes inside the USA and recommends cost-effective fuel stops along the route.

The system:
- Accepts start and destination locations
- Fetches driving route using OpenRouteService
- Suggests cheapest fuel stops
- Calculates estimated fuel cost
- Assumes:
  - Vehicle range = 500 miles
  - Fuel efficiency = 10 MPG

---

# Features

- Route optimization
- Fuel stop recommendations
- Fuel cost estimation
- REST API architecture
- Optimized API usage
- Local fuel dataset processing

---

# Technologies Used

- Python
- Django
- Django REST Framework
- Pandas
- OpenRouteService API
- Geopy
- Postman

---

# Project Structure

```text
fuel_optimizer/
│
├── fuel_optimizer/
├── routing/
│   ├── services/
│   │   ├── route_service.py
│   │   ├── fuel_service.py
│   │   └── optimizer.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── data/
│   └── fuel-prices-for-be-assessment.csv
│
├── requirements.txt
└── README.md


[loom video](https://www.loom.com/share/781909a5315644e3abfb517652c2523f)
