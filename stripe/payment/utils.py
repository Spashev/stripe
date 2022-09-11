from .models import Item


def calculate_order_amount(item: Item)-> int:
    return int(item.price) * 100
