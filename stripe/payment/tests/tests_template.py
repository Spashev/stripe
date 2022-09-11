from django.test import TestCase
from django.urls import reverse


class TemplateTests(TestCase):

    def test_home_page(self):
        """Testing home page"""
        response = self.client.get(reverse('payment:home'))
        self.assertEqual(response.status_code, 200)

    def test_session_page(self):
        """Testing session page"""
        response = self.client.get(reverse('payment:session'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Payment session', str(response.content))

    def test_intent_page(self):
        """Testing intent page"""
        response = self.client.get(reverse('payment:intent'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Payment intent', str(response.content))
