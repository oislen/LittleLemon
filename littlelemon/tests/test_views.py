from django.test import TestCase
from restaurant.models import Menu

class MenuItemsViews(TestCase):
    def setUp(self):
        greek_salad = Menu.objects.create(dish='Greek Salad', price=12.00, inventory=2)
        fish = Menu.objects.create(dish='Fish', price=15.00, inventory=10)
    
    def test_menu_items_list(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Greek Salad')
        self.assertContains(response, 'Fish')