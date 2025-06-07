from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
   title = models.CharField(max_length=255, db_index=True)

class MenuItem(models.Model):
   reference = models.CharField(max_length=32, db_index=True)
   name = models.CharField(max_length=255, db_index=True)
   category = models.ForeignKey(Category, on_delete=models.PROTECT, default=None)
   description = models.TextField(max_length=1020, default=None, null=True)
   ingredients = models.CharField(max_length=510, default=None, null=True)
   price = models.DecimalField(max_digits=6, decimal_places=2, default=None, null=True)
   quantity = models.SmallIntegerField(default=None, null=True)
   date_added = models.DateField()
   featured = models.BooleanField(default=False)

class Booking(models.Model):
   full_name = models.CharField(max_length=255)
   mobile_number = models.CharField(max_length=32)
   guest_number = models.PositiveIntegerField()
   date_time = models.DateTimeField()
   comment = models.CharField(max_length=1020, default=None, null=True, blank=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.SmallIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('menu_item', 'user')

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    delivery_crew = models.ForeignKey(User, on_delete=models.PROTECT, related_name="delivery_crew", null=True)
    status = models.CharField(max_length=32, default="pending")
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date_time = models.DateTimeField()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='order')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('order', 'menu_item')