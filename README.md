# Travel Booking Application

A simple **Travel Booking Web Application** built with **Python Django**, allowing users to view available travel options, book tickets, and manage their bookings. The frontend is developed using **Django Templates** and **Bootstrap** for responsive design.

---

## Features

### User Management
- User registration, login, and logout using Django’s built-in authentication system.
- Update and manage user profile information.

### Travel Options
- Browse available travel options: **Flights, Trains, Buses**.
- View details like source, destination, date, time, price, and available seats.

### Booking Management
- Book travel tickets.
- View and manage your bookings.
- Cancel bookings (optional based on project setup).

---

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** Django Templates, HTML, CSS, Bootstrap
- **Database:** SQLite (default, can be changed to PostgreSQL or MySQL)
- **Authentication:** Django’s built-in authentication system

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AkhilChauhan-UK/travel-booking.git
Navigate to the project folder:

bash
Copy code
cd travel-booking

Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Create a superuser (for admin access):

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Open your browser and go to:

cpp
Copy code
http://127.0.0.1:8000/
Project Structure
php
Copy code
travel_booking/
├── travel_booking/      # Django project settings
├── bookings/            # App for handling bookings
├── travel/              # App for travel options
├── templates/           # HTML templates
├── static/              # CSS, JS, images
├── manage.py
└── requirements.txt
