from django.db import models


class VendingMachine(models.Model):
    name = models.CharField(max_length=100)
    coin = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

    def add_coin(self, coins):
        self.coin += coins
        return self.coin

    def return_coin(self):
        coins_returned = self.coin
        self.coin = 0
        return coins_returned

    def purchase(self):
        self.coin -= 2
        return self.coin



class Inventory(models.Model):
    name = models.CharField(max_length=100)
    machine_name = models.OneToOneField(VendingMachine, on_delete=models.CASCADE, null=True, blank=True)
    soda_count = models.PositiveIntegerField(default=5, null=False, blank=False)
    water_count = models.PositiveIntegerField(default=5, null=False, blank=False)
    juice_count = models.PositiveIntegerField(default=5, null=False, blank=False)

    def __str__(self):
        return self.name

    def purchase_success(self, id):
        pass



class Beverage(models.Model):
    
    typeofbeverage = (
        ('SODA', 'SODA'),
        ('WATER', 'WATER'),
        ('JUICE', 'JUICE'),
    )

    name = models.CharField(max_length=5, choices=typeofbeverage, null=True, blank=True)
    cost = models.IntegerField(default=2)
    inventory_name = models.ForeignKey('Inventory', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name





