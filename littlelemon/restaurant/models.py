from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, db_index=True)

class MenuItem(models.Model):
    menuitem_id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=32, db_index=True)
    name = models.CharField(max_length=255, db_index=True)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, default=None)
    description = models.TextField(max_length=1020, default=None, null=True)
    ingredients = models.CharField(max_length=510, default=None, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=None, null=True)
    quantity = models.SmallIntegerField(default=None, null=True)
    date_added = models.DateField()
    featured = models.BooleanField(default=False)

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=32)
    guest_number = models.PositiveIntegerField()
    date_time = models.DateTimeField()
    comment = models.CharField(max_length=1020, default=None, null=True, blank=True)

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer_username = models.ForeignKey(User, on_delete=models.PROTECT)
    menuitem_id = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.SmallIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_username = models.ForeignKey(User, on_delete=models.PROTECT)
    delivery_username = models.ForeignKey(User, on_delete=models.PROTECT, related_name="delivery_crew", null=True)
    status = models.CharField(max_length=32, default="pending")
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date_time = models.DateTimeField()

class OrderItem(models.Model):
    orderitem_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='order')
    menuitem_id = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)