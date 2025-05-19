from django.test import TestCase
from restaurant.models import Menu

class MenuTestCase(TestCase):
    def test_get_item(self):
        menuItem = Menu(dish='Greek Salad', price=12.00, inventory=2)
        self.assertEqual(str(menuItem), 'Greek Salad : 12.00')