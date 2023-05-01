from django.db import models

# Create your models here.
class Chat(models.Model):
    summary = models.CharField(max_length=300)
    person = models.CharField(max_length=200, null='True')
