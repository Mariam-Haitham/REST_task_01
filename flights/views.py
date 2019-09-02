from rest_framework.generics import ListAPIView
from .serializers import FlightListSerializer, BookingListSerializer
from .models import Flight, Booking
from django.utils import timezone

class HotelListView (ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightListSerializer

class BookingListView (ListAPIView):
	queryset = Booking.objects.filter(date__gte = timezone.now())
	serializer_class = BookingListSerializer


