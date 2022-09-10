from django.urls import path
from .views import HomePageView, StripeSessionsView, ItemDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('item/<slug:slug>', ItemDetailView.as_view(), name='item-detail'),
    path('payment', StripeSessionsView.as_view(), name='stripe-sessions')
]
