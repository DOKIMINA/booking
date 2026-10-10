from django.shortcuts import render
from .models import Apart, Booking
# Create your views here.
def home(request):
    aparts = Apart.objects.all()
    return render(request, 'home.html', {'aparts' : aparts})


def apart_page(request, id):
    apartment = Apart.objects.get(id=id)
    return render(request, 'apartment_page.html', {'apartment' : apartment})