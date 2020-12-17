from django.db import models
# Create your models here.
from accounts.models import UserProfile


class Mail(models.Model):
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    sender = models.CharField(max_length=30, blank=False)
    title = models.CharField(max_length=30, blank=False)
    content = models.TextField(blank=False)

    def __str__(self):
        return f'Sender: {self.sender} Receiver: {self.receiver} Title: {self.title} Content: {self.content}'


class IsRead(models.Model):
    mail = models.ForeignKey(Mail, on_delete=models.CASCADE)
    isread = models.CharField(max_length=6)
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
