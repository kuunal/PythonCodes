from django.urls import path
from .views import ParkingView
from rest_framework import routers
from .views import ParkingView, VehicleTypeView, ParkingTypeView, ParkingLotView, ParkingSlotView
from django.urls import path, include
from vehicle.views import VehicleView


router = routers.DefaultRouter()
router.register('park', ParkingView)
router.register('vehicletype', VehicleTypeView)
router.register('parkingtype', ParkingTypeView)
router.register('parked', ParkingSlotView)


vehicle_router = routers.DefaultRouter()
vehicle_router.register('park', VehicleView)

lot = routers.DefaultRouter()
lot.register('', ParkingLotView)

urlpatterns = [
    path('park/', include(router.urls)),
    path('register/', include(vehicle_router.urls)),
    path('', include(lot.urls), name="lot")     
]
