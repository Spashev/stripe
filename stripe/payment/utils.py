from .models import Item


def calculate_order_amount(item: Item, quantity: int)-> int:
    return int(item.price) * int(quantity)
