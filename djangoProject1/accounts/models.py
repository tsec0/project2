from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=15, blank=True)
    last_name = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=40, blank=True)
    mobile = models.CharField(max_length=10, blank=True)

    profile_picture = models.ImageField(
        upload_to='users',
        blank=True,
    )

    def __str__(self):
        return f'User: {self.user.username}'
