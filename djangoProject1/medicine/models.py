from django.db import models


class Medicine(models.Model):

    G = 'grams'
    LB = 'pounds'
    OUN = 'ounces'

    MEDICINE_QUANTITY = (
        (G, 'Grams'),
        (LB, 'Pounds'),
        (OUN, 'Ounces')
    )

    LEV = 'lev'
    DOLLAR = 'dollar'
    EURO = 'euro'

    MONEY = (
        (LEV, 'Lev'),
        (DOLLAR, '$'),
        (EURO, 'Euro')
    )

    medicine_name = models.CharField(max_length=15, blank=False)
    ingredients = models.CharField(max_length=15, blank=False)
    description = models.TextField(blank=False)
    suitable_for = models.CharField(max_length=100, blank=False)
    manufacturer = models.CharField(max_length=30, blank=False)
    weight = models.IntegerField(blank=False)
    weight_tag = models.CharField(max_length=12, choices=MEDICINE_QUANTITY, default=G)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False)
    price_tag = models.CharField(max_length=12, choices=MONEY, default=DOLLAR)

    image = models.ImageField(
        upload_to='medicine',
        blank=False
    )
    image_one = models.ImageField(
        upload_to='medicine',
        blank=False
    )
    image_two = models.ImageField(
        upload_to='medicine',
        blank=False
    )
    image_three = models.ImageField(
        upload_to='medicine',
        blank=False
    )

    def __str__(self):
        return f'{self.medicine_name} {self.manufacturer} {self.ingredients} ' \
               f'{self.weight}{self.weight_tag} {self.price}{self.price_tag}'
