from django.test import TestCase
from payment.models import Item


class TemplateTests(TestCase):

    def setUp(self):
        Item.objects.create(name="lion", description="roar", price=2000)
        Item.objects.create(name="cat", description="meow", price=1000)

    def test_items_description(self):
        """Item description testing"""
        lion = Item.objects.get(name="lion")
        cat = Item.objects.get(name="cat")
        self.assertEqual(lion.description, "roar")
        self.assertEqual(cat.description, "meow")

    def test_items_price(self):
        """Item price testing"""
        lion = Item.objects.get(name="lion")
        cat = Item.objects.get(name="cat")
        self.assertTrue(lion.price > 1000, True)
        self.assertNotEqual(int(lion.price), 1000)