from django.shortcuts import render
from .models import Item


def index(request):
    context = Item.objects.all()
    return render(request, 'payment/index.html', {'items': context})
