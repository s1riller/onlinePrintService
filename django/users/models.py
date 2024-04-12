# models.py в вашем приложении
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from django.utils.crypto import get_random_string

from .utils import NextCloud


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)
    password_nextcloud = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        # Check if the user is already in the database
        if self.pk:
            orig = CustomUser.objects.get(pk=self.pk)
            if orig.password != self.password:
                self.set_password(self.password)  # Hash new password if changed
        else:
            self.set_password(self.password)  # Hash password for new user

        super().save(*args, **kwargs)  # Call the "real" save() method.


@receiver(post_save, sender=CustomUser)
def create_nextcloud_user(sender, instance, created, **kwargs):
    if created:
        NextCloud.enable_user(instance.username)
        NextCloud.create_user(instance.username, instance.password_nextcloud)

@receiver(post_delete, sender=CustomUser)
def delete_nextcloud_user(sender, instance, **kwargs):
    NextCloud.disable_user(instance.username)


class File(models.Model):
    name = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='files')
    url = models.TextField()

    def __str__(self):
        return self.name


@receiver(post_save, sender=File)
def upload_nextcloud_file(sender, instance, created, **kwargs):

    NextCloud.upload_file()


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar_url = models.URLField(blank=True, null=True)
