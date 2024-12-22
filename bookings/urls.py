from django.urls import path
from . import views

urlpatterns = [
    path('repairman/', views.repairman_search, name='repairman_search'),
    path('book/<int:repairman_id>/', views.book_appointment, name='book_appointment'),
    
]
