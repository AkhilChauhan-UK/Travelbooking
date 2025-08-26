from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # User Management
    path("register/", views.register, name="register"),
    
    path("profile/", views.profile, name="profile"),

    # Travel Options
    path("", views.travel_options, name="travel_options"),
    path("travels/", views.travel_options, name="travel_options"),
    path("book/<int:pk>/", views.book_travel, name="book_travel"),

    # Bookings
    path("my_bookings/", views.my_bookings, name="my_bookings"),
    path("cancel/<int:pk>/", views.cancel_booking, name="cancel_booking"),



     # Login & Logout
    path("login/", auth_views.LoginView.as_view(template_name="booking/login.html"), name="login"),
    path("logout/", views.logout_view, name="logout"),
]
