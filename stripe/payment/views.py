from django.shortcuts import get_object_or_404
from django.conf import settings
from django.views.generic import TemplateView, DetailView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
DOMAIN = 'http://127.0.0.1:8000'


class HomePageView(TemplateView):
    template_name = 'payment/home.html'


class SessionPageView(TemplateView):
    template_name = 'payment/session/session.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['items'] = Item.objects.all()
        return context


class IntentPageView(TemplateView):
    template_name = 'payment/intent/intent.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['items'] = Item.objects.all()
        return context


class ItemDetailView(DetailView):
    model = Item
    template_name = 'payment/session/detail.html'
    slug_field = 'slug'
    context_object_name = 'item'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'public_key': settings.STRIPE_PUBLIC_KEY
        })
        print(context)
        return context


class StripeSessionView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            item_id = kwargs.get('id', None)
            if item_id is not None:
                item = get_object_or_404(Item, id=item_id)
                print(item)
                checkout_session = stripe.checkout.Session.create(
                    line_items=[
                        {
                            'price_data': {
                                'currency': 'kzt',
                                'unit_amount': int(item.price) * 100,
                                'product_data': {
                                    'name': item.name
                                }
                            },
                            'quantity': 1,
                        },
                    ],
                    mode='payment',
                    success_url=DOMAIN + '/success/',
                    cancel_url=DOMAIN + '/cancel/',
                    metadata={
                        item_id: item.id
                    }
                )
                return Response({'message': checkout_session.url}, status.HTTP_201_CREATED)
            return Response({'error': 'Not enough data'}, status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_403_FORBIDDEN)


class StripeIntentView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            item_id = kwargs.get('id', None)
            if item_id is not None:
                item = get_object_or_404(Item, id=item_id)
                print(item)
                checkout_session = stripe.checkout.Session.create(
                    line_items=[
                        {
                            'price_data': {
                                'currency': 'kzt',
                                'unit_amount': int(item.price) * 100,
                                'product_data': {
                                    'name': item.name
                                }
                            },
                            'quantity': 1,
                        },
                    ],
                    mode='payment',
                    success_url=DOMAIN + '/success/',
                    cancel_url=DOMAIN + '/cancel/',
                    metadata={
                        item_id: item.id
                    }
                )
                return Response({'message': checkout_session.url}, status.HTTP_201_CREATED)
            return Response({'error': 'Not enough data'}, status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_403_FORBIDDEN)


class SuccessView(TemplateView):
    template_name = 'payment/success.html'


class ErrorView(TemplateView):
    template_name = 'payment/error.html'


class CancelView(TemplateView):
    template_name = 'payment/cancel.html'
