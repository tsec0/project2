from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    profile_picture = models.ImageField(
        upload_to='users',
        blank=True
    )
    first_name = models.CharField(max_length=15, blank=True)
    middle_name = models.CharField(max_length=15, blank=True)
    last_name = models.CharField(max_length=15, blank=True)
    age = models.CharField(max_length=3)
    mobile_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username
