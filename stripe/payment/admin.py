from django.contrib import admin
from .models import UserModel, Item, Order


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ("user", "address", "balance")
    list_filter = ("user", "address",)
    search_fields = ("user", "balance")


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price")
    list_filter = ("name", "price",)
    search_fields = ("name", "price")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("status", "user", "item")
    list_filter = ("status", "user", "item")
    search_fields = ("item", "user")
