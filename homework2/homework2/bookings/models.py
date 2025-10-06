from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.CharField(max_length=5) # format "HH:MM"

    def __str__(self):
        return self.title\
    
class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"self.seat_number - {'Booked' if self.is_booked else 'Available'}"

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DurationField()

    def __str__(self):
        return f"{self.user.username} booked {self.seat.seat_number} for {self.movie.title}"