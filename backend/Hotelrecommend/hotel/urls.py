from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, UserViewSet, BookingViewSet, ActivityViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'hotels', HotelViewSet, basename='hotel')
router.register(r'users', UserViewSet, basename='user')
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'activities', ActivityViewSet, basename='activity')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
