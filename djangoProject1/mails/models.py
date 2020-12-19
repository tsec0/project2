from django.db import models
# Create your models here.
from accounts.models import UserProfile


class Mail(models.Model):
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    sender = models.CharField(max_length=30, blank=False)
    title = models.CharField(max_length=30, blank=False)
    quantity = models.PositiveIntegerField(blank=False, default=1)
    content = models.TextField(blank=False)
    address = models.CharField(max_length=100, blank=False)
    offer = models.PositiveIntegerField(blank=False, default=0)

    def __str__(self):
        return f'Sender: {self.sender} Receiver: {self.receiver} Title: {self.title} Content: {self.content}'


class IsRead(models.Model):
    mail = models.ForeignKey(Mail, on_delete=models.CASCADE)
    isread = models.CharField(max_length=6)
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
