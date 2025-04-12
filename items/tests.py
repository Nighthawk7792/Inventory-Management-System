from django.test import TestCase
from django.urls import reverse
from .models import Item

class ItemModelTest(TestCase):
    def setUp(self):
        Item.objects.create(name="Test Item", quantity=10, price=9.99)

    def test_item_creation(self):
        item = Item.objects.get(id=1)
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.inventory_value, 99.9)

class ViewTests(TestCase):
    def test_item_list_view(self):
        response = self.client.get(reverse('items:item_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Inventory Items")
        self.assertTemplateUsed(response, 'items/item_list.html')
        