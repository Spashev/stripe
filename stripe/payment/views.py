from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView, DetailView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item

import json
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
DOMAIN = 'http://127.0.0.1:8000'


class HomePageView(TemplateView):
    template_name = 'payment/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['items'] = Item.objects.all()
        return context


class ItemDetailView(DetailView):
    model = Item
    template_name = 'payment/detail.html'
    slug_field = 'slug'
    context_object_name = 'item'


class StripeSessionsView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.data)
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': '{{PRICE_ID}}',
                        'price_data': {
                            'currency': 'kzt',
                            'unit_amount': 2000,
                            'product_data': {
                                'name': 'Test name',
                            }
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=DOMAIN + '/success/',
                cancel_url=DOMAIN + '/cancel/',
            )
            return Response({'message': checkout_session.url}, status.HTTP_303_SEE_OTHER)
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_400_BAD_REQUEST)

    @classmethod
    def calculate_order_amount(cls, items):
        # Replace this constant with a calculation of the order's amount
        # Calculate the order total on the server to prevent
        # people from directly manipulating the amount on the client
        return 1400
