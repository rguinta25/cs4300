from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Movie, Seat, Booking

# ------------------------------
# Unit Tests for Models
# ------------------------------
class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test Description",
            release_date="2025-10-05",
            duration=120
        )

    def test_movie_creation(self):
        movie = Movie.objects.get(title="Test Movie")
        self.assertEqual(movie.duration, 120)
        self.assertEqual(str(movie), "Test Movie")


class SeatModelTest(TestCase):
    def setUp(self):
        self.seat = Seat.objects.create(seat_number="A1")

    def test_seat_creation(self):
        self.assertFalse(self.seat.is_booked)
        self.assertEqual(str(self.seat), "A1")


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test Desc",
            release_date="2025-10-05",
            duration=120
        )
        self.seat = Seat.objects.create(seat_number="A1")
        self.booking = Booking.objects.create(
            movie=self.movie, seat=self.seat, user=self.user
        )

    def test_booking_creation(self):
        self.assertEqual(str(self.booking), "testuser - Test Movie - A1")
        self.assertEqual(self.booking.movie.title, "Test Movie")
        self.assertEqual(self.booking.seat.seat_number, "A1")
        self.assertEqual(self.booking.user.username, "testuser")


# ------------------------------
# Integration Tests for API
# ------------------------------
class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="apiuser", password="12345")
        self.client.login(username="apiuser", password="12345")

        self.movie = Movie.objects.create(
            title="API Movie", description="API Desc", release_date="2025-10-05", duration=90
        )
        self.seat = Seat.objects.create(seat_number="B1")

    # --- Movie API ---
    def test_get_movies(self):
        response = self.client.get("/api/movies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_movie(self):
        response = self.client.post("/api/movies/", {
            "title": "New Movie",
            "description": "New Desc",
            "release_date": "2025-12-01",
            "duration": 100
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)

    # --- Seat API ---
    def test_get_seats(self):
        response = self.client.get("/api/seats/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_book_seat(self):
        response = self.client.post("/api/bookings/", {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "user": self.user.id
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        booking = Booking.objects.get(movie=self.movie, seat=self.seat, user=self.user)
        self.assertIsNotNone(booking)

    # --- Booking History API ---
    def test_get_booking_history(self):
        Booking.objects.create(movie=self.movie, seat=self.seat, user=self.user)
        response = self.client.get("/api/bookings/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
