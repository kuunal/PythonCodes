from django.urls import path
from .views import ParkingView
from rest_framework import routers
from .views import ParkingView, VehicleTypeView, ParkingTypeView, ParkingLotView
from django.urls import path, include
from vehicle.views import VehicleView


router = routers.DefaultRouter()
router.register('', ParkingView)
router.register('vehicletype', VehicleTypeView)
router.register('parkingtype', ParkingTypeView)


vehicle_router = routers.DefaultRouter()
vehicle_router.register('', VehicleView)

lot = routers.DefaultRouter()
lot.register('', ParkingLotView)

urlpatterns = [
    path('park/', include(router.urls)),
    path('register/', include(vehicle_router.urls)),
    path('', include(lot.urls), name="lot")     
]
