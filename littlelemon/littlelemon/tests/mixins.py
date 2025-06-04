from django.test import Client
from restaurant.models import Booking, MenuItem, Category
from random import randint

BOOKINGS = {
    1: {"first_name": "Adam", "last_name": "Byrne", "guest_number": randint(1, 11), "date_time":"2023-03-04 09:00:00", "comment":"Wedding"},
    2: {"first_name": "Jake", "last_name": "Nelson", "guest_number": randint(1, 11), "date_time":"2024-01-10 12:00:00", "comment":"Funeral"},
    3: {"first_name": "Sinead", "last_name": "Bughes", "guest_number": randint(1, 11), "date_time":"2025-12-20 14:00:00", "comment":"Christening"},
}

MENU_ITEMS = {
    1: {"name": "Apple Pie", "price": 13.78, "quantity": randint(0, 11), "description":"Baked apple pie with cream", "category":"Dessert"},
    2: {"name": "Vanilla Latte", "price": 3.99, "quantity": randint(0, 11), "description":"Barista latte with vanilla essence" , "category":"Drinks"},
    3: {"name": "Ice-cream", "price": 5.00, "quantity": randint(0, 11), "description":"Chocolate, strawberry ot vanilla", "category":"Dessert"},
}

class BookingMixin:
    bookings = BOOKINGS

    def create_bookings(self):
        for idx in self.bookings.keys():
            booking = Booking.objects.create(
                first_name = self.bookings[idx]["first_name"],
                last_name = self.bookings[idx]["last_name"],
                guest_number = self.bookings[idx]["guest_number"],
                date_time = self.bookings[idx]["date_time"],
                comment = self.bookings[idx].get("comment", None),
            )
            booking.save()

class SingleBookingMixin:
    booking = BOOKINGS.get(1)

    def create_booking(self):
        booking = Booking.objects.create(
            first_name = self.booking.get("first_name"),
            last_name = self.booking.get("last_name"),
            guest_number = self.booking.get("guest_number"),
            date_time = self.booking.get("date_time"),
            comment = self.booking.get("comment", None),
        )
        booking.save()
        self.booking = booking

class MenuItemMixin:
    items = MENU_ITEMS

    def create_menu_items(self):
        for idx in self.items.keys():
            # create category
            category = Category.objects.create(
                title=self.items[idx].get("category"),
                slug = self.items[idx].get("category").lower().replace(" ", "-")
                )
            # create menu item
            item = MenuItem.objects.create(
                name = self.items[idx]["name"],
                price = self.items[idx]["price"],
                quantity = self.items[idx].get("quantity", None),
                description = self.items[idx].get("description", None),
                featured = self.items[idx].get("featured", False),
                category = category
            )
            item.save()


class SingleMenuItemMixin:
    item = MENU_ITEMS.get(1)

    def create_menu_item(self):
        # create category
        category = Category.objects.create(
            title=self.item.get("category"),
            slug = self.item.get("category").lower().replace(" ", "-")
            )
        # create menu item
        item = MenuItem.objects.create(
            name = self.item["name"],
            price = self.item["price"],
            description = self.item.get("description", None),
            quantity = self.item.get("quantity", None),
            featured = self.item.get("featured", False),
            category = category
        )
        item.save()
        self.menu_item = item