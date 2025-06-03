from django.forms import ModelForm, DateTimeInput
from .models import Booking
from django.contrib.admin.widgets import AdminDateWidget


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    input_type ='datetime-local'
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            'date_time': DateTimeInput(attrs={'type': 'datetime-local'})
        }
