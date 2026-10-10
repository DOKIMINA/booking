from django.urls import path
from .views import home, apart_page

urlpatterns = [
    path('', home, name='home'),
    path('apartments/<int:id>/', apart_page, name='apart_page' ),
]