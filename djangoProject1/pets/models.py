from django.db import models

from accounts.models import UserProfile


class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'
    MOUSE = 'mouse'
    SPIDER = 'spider'
    SNAKE = 'snake'
    LIZARD = 'lizard'
    CHAMELEON = 'chameleon'
    FISH = 'fish'
    MONKEY = 'monkey'

    PET_TYPES = (
        (DOG, 'Dog'), (CAT, 'Cat'), (PARROT, 'Parrot'), (MOUSE, 'Mouse'),
        (SPIDER, 'Spider'), (SNAKE, 'Snake'), (LIZARD, 'Lizard'),
        (CHAMELEON, 'Chameleon'), (FISH, 'Fish'), (MONKEY, 'Monkey'),
    )

    animal = models.CharField(max_length=20, choices=PET_TYPES, default=DOG)
    animal_type = models.CharField(max_length=30, blank=False)
    name = models.CharField(max_length=15, blank=False)
    age = models.IntegerField(blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False)
    price_tag = '$'
    image = models.ImageField(
        upload_to='pets',
        blank=False
    )
    image_one = models.ImageField(
        upload_to='pets',
        blank=False
    )
    image_two = models.ImageField(
        upload_to='pets',
        blank=False
    )
    image_three = models.ImageField(
        upload_to='pets',
        blank=False
    )
    image_four = models.ImageField(
        upload_to='pets',
        blank=False
    )
    image_five = models.ImageField(
        upload_to='pets',
        blank=False
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'ID: {self.id} Name: {self.name} Age: {self.age} ' \
               f'Animal: {self.animal} Price: {self.price}{self.price_tag}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    like = models.CharField(max_length=4)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Sell(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    sell = models.CharField(max_length=4)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
