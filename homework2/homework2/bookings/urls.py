from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# API router
router = DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'api/seats', views.SeatViewSet)
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [
    # HTML pages
    path('', views.movie_list, name='movie_list'),
    path('seats/html/<int:movie_id>/', views.seat_list, name='seats'),
    path('booking_history/', views.booking_history, name='booking_history'),

    # API endpoints
    path('api/', include(router.urls)),
]
