from django.db import models

class VendingMachine(models.Model):
    name = models.CharField(max_length=50)

class Drink(models.Model):
    type = models.CharField(max_length=10)