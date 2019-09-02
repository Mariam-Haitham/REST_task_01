
from django.contrib import admin
from django.urls import path
from flights import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights/list/', views.HotelListView.as_view(), name = "flights-list"),
    path('booking/list/', views.BookingListView.as_view(), name = "bookings-list"),
]
