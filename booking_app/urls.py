from django.urls import path
from .views import home, apart_page, booking_page, booking_confirmation

urlpatterns = [
    path('', home, name='home'),
    path('apartments/<int:id>/', apart_page, name='apart_page' ),
    path('booking/<int:id>/', booking_page, name='book' ),
    path('booking_confirmation/<int:id>', booking_confirmation, name='booking_confirmation'),
]    
