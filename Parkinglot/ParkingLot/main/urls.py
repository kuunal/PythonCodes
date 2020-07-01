from django.urls import path
from .views import ParkingView
from rest_framework import routers
from .views import ParkingView, VehicleTypeView, ParkingTypeView
# from .views import ParkingView
from django.urls import path, include

router = routers.DefaultRouter()
router.register('park', ParkingView)
router.register('vehicletype', VehicleTypeView)
router.register('parkingtype', ParkingTypeView)


urlpatterns = [
    path('park/', include(router.urls))
    
]
