from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(semder, instance, created, **kwargs):
    # Update order total upon lineitem update or creation
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(semder, instance, **kwargs):
    # Update order total upon lineitem deletion
    instance.order.update_total()
