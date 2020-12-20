from django.db import models

# Create your models here.
from accounts.models import UserProfile


class Toys(models.Model):

    toy_name = models.CharField(max_length=15, blank=False)
    material = models.CharField(max_length=15, blank=False)
    description = models.TextField(blank=False)
    suitable_for = models.CharField(max_length=100, blank=False)
    manufacturer = models.CharField(max_length=30, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False)
    price_tag = '$'
    image = models.ImageField(
        upload_to='toys',
        blank=False
    )
    image_one = models.ImageField(
        upload_to='toys',
        blank=False
    )
    image_two = models.ImageField(
        upload_to='toys',
        blank=False
    )
    image_three = models.ImageField(
        upload_to='toys',
        blank=False
    )

    def __str__(self):
        return f'{self.toy_name} {self.manufacturer} {self.material} {self.price}{self.price_tag}'


class Liked(models.Model):
    toy = models.ForeignKey(Toys, on_delete=models.CASCADE)
    liked = models.CharField(max_length=5)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class CommentsOfToys(models.Model):
    toy = models.ForeignKey(Toys, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
