from django.shortcuts import render, redirect
from django.contrib import messages
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
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        phone = request.POST.get('phone')

        existing_booking = Booking.objects.filter(apart=apart, check_in = check_out, check_out = check_in)

        if existing_booking.exists():
            messages.error(request, 'Вже заброньовано')

        else:
            booking = Booking.objects.create(
            apart = apart,
            user = request.user,
            name = full_name,
            email = email,
            phone = phone,
            check_in = check_in,
            check_out = check_out
            )
            return redirect('booking_confirmation', id=booking.id)

    return render(request, 'booking_page.html', {'apartment' : apart})


@login_required
def booking_confirmation(request, id):
    booking = Booking.objects.get(id=id)
    return render(request, 'booking_success.html', {'booking' : booking })