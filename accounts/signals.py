from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile
from .utils import create_avatar


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # print("!!!USER CREATED")
        Profile.objects.create(
            user=instance, profile_image=create_avatar(instance.email)
        )


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # print("!!!USER UPDATED")
    instance.profile.save()
