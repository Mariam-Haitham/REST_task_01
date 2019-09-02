from .models import Flight, Booking
from rest_framework import serializers

class FlightListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		exclude = ['miles']

class BookingListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['id', 'flight', 'date']