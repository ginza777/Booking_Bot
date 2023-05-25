from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Visitor
from .utils import generate_ticket


@receiver(post_save, sender=Visitor)
def create_profile(sender, instance, created, **kwargs):
    if created:
        generate_ticket(instance)
