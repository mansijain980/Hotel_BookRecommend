from rest_framework import serializers
from .models import Hotel, User, Booking, Activity

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'  # Includes all fields from the Hotel model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Includes all fields from the User model

class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested serializer for user
    hotel = HotelSerializer(read_only=True)  # Nested serializer for hotel

    class Meta:
        model = Booking
        fields = '__all__'  # Includes all fields from the Booking model

# class ActivitySerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)  # Nested serializer for user
#     hotel = HotelSerializer(read_only=True)  # Nested serializer for hotel

#     class Meta:
#         model = Activity
#         fields = '__all__'  # Includes all fields from the Activity model
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'user', 'hotel', 'activity_type', 'timestamp']