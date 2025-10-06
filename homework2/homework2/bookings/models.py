from django.db import models
from django.contrib.auth.models import User

from datetime import timedelta
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    duration = models.DurationField()  # stores as timedelta

    def __str__(self):
        return self.title

    
class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.seat_number} - {'Booked' if self.is_booked else 'Available'}"

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.seat.seat_number} - {'Booked' if self.seat.is_booked else 'Available'}"
