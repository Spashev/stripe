from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

from .utils import image_resize


class UserModel(models.Model):
    """
    Custom user model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True, blank=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Item(models.Model):
    """
    Item model.
    """
    name = models.CharField(max_length=150, verbose_name='Item name', help_text='Item name length 150')
    description = models.CharField(max_length=500, verbose_name='Item description')
    price = models.DecimalField(verbose_name='Item price', max_digits=12, decimal_places=2, default=0)
    image = models.ImageField(verbose_name='Item image', upload_to='uploads/%Y/%m/%d/', blank=True, null=True)
    slug = models.SlugField(verbose_name='Item slug', null=True, blank=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        indexes = [
            models.Index(fields=['name', 'price']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('payment:item-detail', kwargs={'slug': self.slug})

    def save(self, commit=True, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Order(models.Model):
    class Status(models.TextChoices):
        in_progress = 'in_progress', 'IP'
        canceled = 'canceled', 'CD'
        new = 'new', 'New'
        arrived = 'arrived', 'Arrived'

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.new)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name
