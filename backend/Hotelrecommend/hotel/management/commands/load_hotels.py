import json
from django.core.management.base import BaseCommand
from hotel.models import Hotel  # Replace 'myapp' with your app name

class Command(BaseCommand):
    help = 'Load hotels data from data.json'

    def handle(self, *args, **kwargs):
        with open(r'C:\Users\MANSI JAIN\OneDrive\Desktop\iconcile_assignment\backend\Hotelrecommend\hotels.json') as f:  # Replace with your data.json file path
            hotels_data = json.load(f)
            for hotel in hotels_data['hotels']:
                Hotel.objects.create(
                    name=hotel['name'],
                    ratings=float(hotel['ratings']),
                    visits=int(hotel['visits']),
                    completed_bookings=int(hotel['completedBookings']),
                    draft_bookings=int(hotel['draftBookings']),
                    tags=hotel['tags'],
                    description=hotel['description'],
                    image_url=hotel['imageUrl']
                )
        self.stdout.write(self.style.SUCCESS('Hotels data loaded successfully'))
