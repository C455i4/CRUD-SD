from django.contrib.auth.models import User, Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomPermissions

@receiver(post_save, sender=User)
def assign_permissions(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        # Adiciona a permissão aos usuários administradores
        instance.user_permissions.add(Permission.objects.get(codename=CustomPermissions.CAN_CRUD_DATA))
