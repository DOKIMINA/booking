from django.shortcuts import render
from .models import Apart, Booking
from django.contrib.auth.decorators import login_required

def home(request):
    aparts = Apart.objects.all()
    return render(request, 'home.html', {'aparts' : aparts})


def apart_page(request, id):
    apartment = Apart.objects.get(id=id)
    return render(request, 'apartment_page.html', {'apartment' : apartment})

@login_required
def booking_page(request, id):
    apart = Apart.objects.get(id=id)
    return render(request, 'booking_page.html', {'apartment' : apart})
