from django.db import models


# Create your models here.
from accounts.models import UserProfile


class UserFeedBack(models.Model):

    publisher = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=False)
    servicing = models.DecimalField(max_digits=3, decimal_places=1, blank=False)
    mailing = models.DecimalField(max_digits=3, decimal_places=1, blank=False)
    publishing = models.DecimalField(max_digits=3, decimal_places=1, blank=False)
    orders = models.DecimalField(max_digits=3, decimal_places=1, blank=False)
    content = models.TextField(blank=True)

    def __str__(self):
        return f'Publisher: {self.publisher} Title: {self.title} ' \
               f'Mark Servicing: {self.servicing} ' \
               f'Mark Mailing: {self.mailing} ' \
               f'Mark Publishing: {self.publishing} ' \
               f'Mark Orders: {self.orders} '
