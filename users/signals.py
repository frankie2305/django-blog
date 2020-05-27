from django.contrib import messages
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(user_logged_in, sender=User)
def logged_in_message(sender, request, user, **kwargs):
    messages.success(request, f'Welcome, {user.username}! Thanks for logging in!')

@receiver(user_logged_out, sender=User)
def logged_out_message(sender, request, user, **kwargs):
    messages.info(request, f'{user.username} has been logged out!')
