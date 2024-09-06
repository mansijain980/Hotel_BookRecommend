from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Hotel, User, Booking, Activity
from .serializers import HotelSerializer, UserSerializer, BookingSerializer, ActivitySerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    @action(detail=True, methods=['post'])
    def visit(self, request, pk=None):
        hotel = self.get_object()
        user = User.objects.get(id=request.data.get('user_id'))
        hotel.visits += 1
        hotel.save()
        Activity.objects.create(user=user, hotel=hotel, activity_type='visit')
        return Response({'status': 'Hotel visited'})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.get(id=request.data.get('user_id'))
        hotel = Hotel.objects.get(id=request.data.get('hotel_id'))
        status_choice = request.data.get('status', 'draft')
        
        if status_choice == 'completed':
            hotel.completed_bookings += 1
        else:
            hotel.draft_bookings += 1
        
        hotel.save()

        booking = Booking.objects.create(user=user, hotel=hotel, status=status_choice)
        Activity.objects.create(user=user, hotel=hotel, activity_type=f"{status_choice}_booking")
        serializer = self.get_serializer(booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    @action(detail=False, methods=['get'])
    def recent(self, request):
        activities = Activity.objects.order_by('-timestamp')[:10]
        serializer = self.get_serializer(activities, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
# URLs Configuration
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'users', UserViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'activities', ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
