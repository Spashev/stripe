from django.urls import path

from .views import (
    HomePageView,
    StripeSessionsView,
    ItemDetailView,
    SuccessView,
    ErrorView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('item/<slug:slug>', ItemDetailView.as_view(), name='item-detail'),
    path('buy/<int:id>', StripeSessionsView.as_view(), name='stripe-sessions'),
    path('success/', SuccessView.as_view(), name='success'),
    path('error/', ErrorView.as_view(), name='error')
]
