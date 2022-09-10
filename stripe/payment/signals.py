from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import UserModel


@receiver(post_save, sender=User)
def create(sender, instance, created, **kwargs):
    if created:
        UserModel.objects.create(user=instance)


@receiver(post_save, sender=User)
def save(sender, instance, **kwargs):
    instance.usermodel.save()
