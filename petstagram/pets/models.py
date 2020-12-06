from django.db import models

from accounts.models import UserProfile


class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'
    MOUSE = 'mouse'
    SPIDER = 'spider'
    UNKNOWN = 'unknown'

    PET_TYPES = (
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (PARROT, 'Parrot'),
        (MOUSE, 'Mouse'),
        (SPIDER, 'Spider'),
        (UNKNOWN, 'Unknown'),
    )

    type = models.CharField(max_length=17, choices=PET_TYPES, default=UNKNOWN)
    name = models.CharField(max_length=16, blank=False)
    age = models.IntegerField(blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=1, blank=False)
    price_tag = '$'
    image = models.ImageField(
        upload_to='pets',
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'ID: {self.id} Name: {self.name} Age: {self.age} ' \
               f'Type: {self.type} Price: {self.price}{self.price_tag}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    test = models.CharField(max_length=2)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
