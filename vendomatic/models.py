from django.db import models
from django.forms import IntegerField


class VendingMachine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    coin_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Beverage(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    cost = models.IntegerField(default=2)
    items_remaining = models.IntegerField()
    machine = models.ForeignKey('VendingMachine', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.type


