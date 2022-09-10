from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    """
    Custom user model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True, blank=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Item(models.Model):
    """
    Item model.
    """
    name = models.CharField(max_length=150, verbose_name='Item name', help_text='Item name length 150')
    description = models.CharField(max_length=500, verbose_name='Item description')
    price = models.FloatField(verbose_name='Item price')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        indexes = [
            models.Index(fields=['name', 'price']),
        ]

    def __str__(self):
        return self.name


class Order(models.Model):
    class Status(models.TextChoices):
        in_progress = 'in_progress', 'IP'
        canceled = 'canceled', 'CD'
        new = 'new', 'New'
        arrived = 'arrived', 'Arrived'

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.new)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
