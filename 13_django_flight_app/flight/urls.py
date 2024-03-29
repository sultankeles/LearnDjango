from django.urls import path, include

from rest_framework import routers

from .views import FlightView, ReservationView


router = routers.DefaultRouter()
router.register('flight', FlightView)
router.register('reservation', ReservationView)

urlpatterns = [
    path('', include(router.urls)),
] # + router.urls
