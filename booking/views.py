from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, BookingForm
from .models import TravelOption, Booking


def logout_view(request):
    logout(request)
    return redirect('login')



# User Registration
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('travel_options')
    else:
        form = UserRegisterForm()
    return render(request, 'booking/register.html', {'form': form})

# Profile Update
@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated!")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'booking/profile.html', {'form': form})

# List Travel Options
def travel_options(request):
    travels = TravelOption.objects.all()
    return render(request, 'booking/travel_options.html', {'travels': travels})

# Book Travel
@login_required
def book_travel(request, pk):
    travel = get_object_or_404(TravelOption, pk=pk)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.travel_option = travel
            booking.total_price = travel.price * booking.number_of_seats
            if booking.number_of_seats <= travel.available_seats:
                travel.available_seats -= booking.number_of_seats
                travel.save()
                booking.save()
                return redirect('my_bookings')
            else:
                messages.error(request, "Not enough seats available.")
    else:
        form = BookingForm()
    return render(request, 'booking/book_travel.html', {'form': form, 'travel': travel})

# My Bookings
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

# Cancel Booking
@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    booking.status = "Cancelled"
    booking.travel_option.available_seats += booking.number_of_seats
    booking.travel_option.save()
    booking.save()
    return redirect('my_bookings')
