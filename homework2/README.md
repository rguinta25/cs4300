# Booking App

Table of Contents:
- [Description](#Description)
- [Features](#Features)
- [Requirements](#Requirements)
- [Setup](#Setup)
- [Usage](#Usage)
- [Testing](#Testing)
- [Render Deployment](#Render_Deployment)

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

## Requirements
- Python 3.x
- Django 4.x
- Django REST Framework
- Bootstrap 5.x
- SQLite

## Setup
1. Clone
git clone https://github.com/rguinta25/cs4300.git
git checkout Homework2
2. Virtual Enviroment
python3 -m venv myenv --system-site-packages
source myenv/bin/activate
2. Install Requirements
pip install -r requirements.txt
4. Database migrations
python manage.py makemigrations
python manage.py migrate
5. Create superuser
python manage.py createsuperuser
6. Run server
python manage.py runserver 0.0.0.0:3000

## Usage
1. Look through home page for available movies
2. Click book Now on movie to select which seat
3. Select available seat and submit
4. View booking history 

## Testing
python manage.py test bookings

## Render Deployment
https://movie-booking-xn9c.onrender.com/
