from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
   slug = models.SlugField()
   title = models.CharField(max_length=255, db_index=True)

class MenuItem(models.Model):
   name = models.CharField(max_length=255, db_index=True)
   price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
   quantity = models.SmallIntegerField(default=0)
   description = models.TextField(max_length=1000, default=None)
   featured = models.BooleanField(db_index=True, default=False)
   category = models.ForeignKey(Category, on_delete=models.PROTECT, default=None)

   def __str__(self):
      return self.name

class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.PositiveIntegerField()
   date_time = models.DateTimeField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        unique_together = ('menuitem', 'user')

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="delivery_crew", null=True)
    status = models.BooleanField(default=0, db_index=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    date = models.DateField(db_index=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        unique_together = ('order', 'menuitem')