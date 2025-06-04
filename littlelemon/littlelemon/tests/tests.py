from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
import json

from api.serializers import MenuItemSerializer, BookingSerializer
from restaurant.models import MenuItem, Booking
from littlelemon.tests.mixins import BookingMixin, SingleBookingMixin, MenuItemMixin, SingleMenuItemMixin

class SetUpMixin:

    def setUp(self):
        username = 'test@email.com'
        password = "testpasswd"
        # create test user
        self.user = User.objects.create_user(username=username, password=password)
        # log in to django client as test user
        self.login = self.client.login(username=username, password=password)

class BookingViewTest(SetUpMixin, BookingMixin, TestCase):

    def setUp(self):
        self.create_bookings()
        return super().setUp()

    def test_list(self):
        response = self.client.get("/api/bookings/")
        serializer = BookingSerializer(Booking.objects.all(), many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_create(self):
        data = {"first_name":"jack", "last_name":"Doe", "guest_number":4, "date_time": "2023-03-04 09:00", "comment":"18th Birthday"}
        response = self.client.post("/api/bookings/", data=data)
        serializer = BookingSerializer(Booking.objects.get(first_name="jack"))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, serializer.data)


class SingleBookingViewTest(SetUpMixin, SingleBookingMixin, TestCase):

    def setUp(self):
        self.create_booking()
        return super().setUp()

    def test_retrieve(self):
        response = self.client.get(f"/api/bookings/{self.booking.pk}/")
        serializer = BookingSerializer(Booking.objects.get(pk=self.booking.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_partial_update(self):
        data = json.dumps({"guest_number": 6, "date_time": "2023-03-06 10:00"})
        response = self.client.patch(f"/api/bookings/{self.booking.pk}/", data=data, content_type="application/json")
        serializer = BookingSerializer(Booking.objects.get(pk=self.booking.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_update(self):
        data = json.dumps({"first_name": "will", "last_name": "Gleeson", "guest_number": 6, "booking_date": "2023-03-06 18:00"})
        response = self.client.put(f"/api/bookings/{self.booking.pk}/", data=data, content_type="application/json")
        serializer = BookingSerializer(Booking.objects.get(pk=self.booking.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_delete(self):
        response = self.client.delete(f"/api/bookings/{self.booking.pk}/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, None)
        self.assertEqual(Booking.objects.filter(pk=self.booking.pk).exists(), False)


class MenuItemViewTest(SetUpMixin, MenuItemMixin, TestCase):

    def setUp(self):
        self.create_menu_items()
        super().setUp()

    def test_list(self):
        response = self.client.get(f"/api/menu-items/")
        serializer = MenuItemSerializer(MenuItem.objects.all(), many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_create(self):
        data = {"name":"Latte", "price":2.99, "quantity":5, "description":"Finely grounded.", "featured":False, "category":"Drinks"}
        response = self.client.post(f"/api/menu-items/", data=data, content_type="application/json")
        serializer = MenuItemSerializer(MenuItem.objects.get(name="latte"))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, serializer.data)


class SingleMenuItemViewTest(SetUpMixin, SingleMenuItemMixin, TestCase):

    def setUp(self):
        self.create_menu_item()
        return super().setUp()

    def test_retrieve(self):
        response = self.client.get(f"/api/menu-items/{self.menu_item.pk}/")
        serializer = MenuItemSerializer(MenuItem.objects.get(pk=self.menu_item.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_partial_update(self):
        data = json.dumps({"price": 3.99, "quantity": 3})
        response = self.client.patch(f"/api/menu-items/{self.menu_item.pk}/", data = data, content_type = "application/json")
        serializer = MenuItemSerializer(MenuItem.objects.get(pk=self.menu_item.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_update(self):
        data = json.dumps({"name": "Apple Juice", "price": 3.85, "quantity": 7, "description": "Freshly squeezed", "category":"Drink"})
        response = self.client.put(f"/api/menu-items/{self.menu_item.pk}/", data = data, content_type = "application/json")
        serializer = MenuItemSerializer(MenuItem.objects.get(pk=self.menu_item.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_delete(self):
        response = self.client.delete(f"/api/menu-items/{self.menu_item.pk}/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, None)
        self.assertEqual(MenuItem.objects.filter(pk=self.menu_item.pk).exists(), False)