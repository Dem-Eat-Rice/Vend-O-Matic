from django.db import models

class VendingMachine(models.Model):
    name = models.CharField(max_length=50)
    coin_count = models.IntegerField(default=0)
    inventory = models.CharField(max_length=500, null=True)

class Beverage(models.Model):
    type = models.CharField(max_length=10)
    cost = models.IntegerField(default=2)
  