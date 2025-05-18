from django.contrib import admin
from .models import Booking
from .models import Menu

# register models
admin.site.register(Menu)
admin.site.register(Booking)