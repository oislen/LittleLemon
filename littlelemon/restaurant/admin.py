from django.contrib import admin
from .models import Booking
from .models import MenuItem
from .models import Category
from .models import Cart
from .models import Order
from .models import OrderItem

# register models
admin.site.register(MenuItem)
admin.site.register(Booking)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)