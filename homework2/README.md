# Booking App

## Description
A Django-based Movie Theater Booking app that allows users to:
- View movie listings
- Book seats
- View booking history

## Features
- View movie listing using API and UI
- Book seats for a selected movie
- CHeck your booking history
- RESTFUL API endpoints for movies, seats, and bookings
- Admin panel from managing movies, seats, and bookings
- User-friendly UI with bootstrap

## Structure
homework2/
├── movie_booking/ project folder
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── bookings/ app
│ ├── models.py # Movie, Seat, Booking models
│ ├── views.py
│ ├── urls.py
│ └── templates/
│ └── bookings/
│ ├── base.html
│ ├── movie_list.html
│ ├── seat_booking.html
│ └── booking_history.html
├── manage.py
└── requirements.txt

## Setup
git clone 