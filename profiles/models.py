from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    user profile to store user information such as purchases made and delivery/billing information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_email = models.EmailField(max_length=254, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)
    default_city = models.CharField(max_length=36, null=True, blank=True)
    default_address = models.CharField(max_length=254, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Creates and/or updates user profile
    if created:
        UserProfile.objects.create(user=instance)
    # for existing users , save the profile
    instance.userprofile.save()
