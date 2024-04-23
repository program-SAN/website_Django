from django.db import models

# Create your models here.

#manually typed
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    text = models.CharField(max_length=120)
    date = models.DateField()

    def __str__(self):
        return self.name