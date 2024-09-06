from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    ratings = models.FloatField()
    visits = models.IntegerField(default=0)
    completed_bookings = models.IntegerField(default=0)
    draft_bookings = models.IntegerField(default=0)
    tags = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=1024)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Booking(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('completed', 'Completed')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.hotel.name} - {self.status}"

class Activity(models.Model):
    ACTIVITY_CHOICES = [
        ('visit', 'Visit'),
        ('draft_booking', 'Draft Booking'),
        ('completed_booking', 'Completed Booking')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.hotel.name} - {self.activity_type}"
