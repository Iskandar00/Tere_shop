from django.db.models.signals import post_delete
from django.dispatch import receiver

from apps.products.services import delete_file_after_delete_obj
from apps.products.models import Product


@receiver(post_delete, sender=Product)
def delete_photo_on_delete_user(instance, *args, **kwargs):
    delete_file_after_delete_obj(instance)
