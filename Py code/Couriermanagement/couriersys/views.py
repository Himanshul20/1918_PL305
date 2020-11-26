from django.shortcuts import render, redirect

from couriersys.forms import BookingForm
# Create your views here.
from couriersys.models import *


def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = BookingForm()
    return render(request, 'BookingForm.html', {'form': form})


def show(request):
    sbook = Booking.objects.all()
    return render(request, "show.html", {'sbook': sbook})
