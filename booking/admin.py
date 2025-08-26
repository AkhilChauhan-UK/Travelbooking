from django.contrib import admin
from .models import TravelOption, Booking

@admin.register(TravelOption)
class TravelOptionAdmin(admin.ModelAdmin):
    list_display = ("travel_id", "travel_type", "source", "destination", "datetime", "price", "available_seats")
    list_filter = ("travel_type", "source", "destination")
    search_fields = ("source", "destination", "travel_type")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("booking_id", "user", "travel_option", "number_of_seats", "total_price", "status", "booking_date")
    list_filter = ("status", "booking_date")
    search_fields = ("user__username", "travel_option__source", "travel_option__destination")
