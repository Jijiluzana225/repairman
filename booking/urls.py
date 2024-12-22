from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('book/<int:repairman_id>/', views.book_appointment, name='book_appointment'),
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='confirmation'),
    path('location/<int:booking_id>/', views.show_location, name='show_location'),
]
