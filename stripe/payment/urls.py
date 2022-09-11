from django.urls import path

from .views import (
    HomePageView,
    StripeSessionView,
    StripeIntentView,
    ItemDetailView,
    SuccessView,
    ErrorView,
    CancelView,
    SessionPageView,
    IntentPageView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('session', SessionPageView.as_view(), name='session'),
    path('intent', IntentPageView.as_view(), name='intent'),
    path('item/<slug:slug>', ItemDetailView.as_view(), name='item-detail'),
    path('buy/<int:id>/session', StripeSessionView.as_view(), name='stripe-sessions'),
    path('buy/<int:id>/intent', StripeIntentView.as_view(), name='stripe-intent'),
    path('success/', SuccessView.as_view(), name='success'),
    path('error/', ErrorView.as_view(), name='error'),
    path('cancel/', CancelView.as_view(), name='cancel'),
]
