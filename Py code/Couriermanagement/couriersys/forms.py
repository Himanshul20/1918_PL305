from django import forms
from couriersys.models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
