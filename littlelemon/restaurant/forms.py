from django.forms import ModelForm, DateTimeInput
from .models import Booking
from django.contrib.admin.widgets import AdminDateWidget


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['comment'].required = False
        self.input_type ='datetime-local'
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            'date_time': DateTimeInput(attrs={'type': 'datetime-local'})
        }
