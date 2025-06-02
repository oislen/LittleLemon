from django.db import models

class Category(models.Model):
   slug = models.SlugField()
   title = models.CharField(max_length=255, db_index=True)

class MenuItem(models.Model):
   name = models.CharField(max_length=255, db_index=True)
   price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
   quantity = models.SmallIntegerField(default=0)
   menu_item_description = models.TextField(max_length=1000, default=None)
   featured = models.BooleanField(db_index=True, default=False)
   category = models.ForeignKey(Category, on_delete=models.PROTECT, default=None)

   def __str__(self):
      return self.name

class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name
