from django.contrib import admin
from .models import Booking
from .models import MenuItem
from .models import Category

# register models
admin.site.register(MenuItem)
admin.site.register(Booking)
admin.site.register(Category)