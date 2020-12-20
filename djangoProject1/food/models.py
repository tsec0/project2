from django.db import models

# Create your models here.
from accounts.models import UserProfile


class Food(models.Model):

    KG = 'kilograms'
    G = 'grams'
    LB = 'pounds'
    OUN = 'ounces'

    FOOD_QUANTITY = (
        (KG, 'Kilograms'), (G, 'Grams'),
        (LB, 'Pounds'), (OUN, 'Ounces')
    )

    food_name = models.CharField(max_length=15, blank=False)
    ingredients = models.CharField(max_length=15, blank=False)
    description = models.TextField(blank=False)
    suitable_for = models.CharField(max_length=100, blank=False)
    manufacturer = models.CharField(max_length=30, blank=False)
    weight = models.IntegerField(blank=False)
    weight_tag = models.CharField(max_length=12, choices=FOOD_QUANTITY, default=G)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False)
    price_tag = '$'
    image = models.ImageField(
        upload_to='food',
        blank=False
    )
    image_one = models.ImageField(
        upload_to='food',
        blank=False
    )
    image_two = models.ImageField(
        upload_to='food',
        blank=False
    )
    image_three = models.ImageField(
        upload_to='food',
        blank=False
    )

    def __str__(self):
        return f'{self.food_name} {self.manufacturer} {self.ingredients}' \
               f' {self.weight}{self.weight_tag} {self.price}{self.price_tag}'


class CommentsOfFood(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
