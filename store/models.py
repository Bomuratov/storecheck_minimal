from django.contrib.auth.models import User
from django.db import models


class Base(models.Model):
    class Meta:
        abstract = True
        ordering = ('id',)


class Territory(models.Model):
    territory_name = models.CharField(max_length=255)

    def __str__(self):
        return self.territory_name


class Trade(models.Model):
    trade_name = models.CharField(max_length=255)

    def __str__(self):
        return self.trade_name


class Sku(models.Model):
    img = models.FileField(upload_to='media/%y/%m/%d/', default='default.png', blank=True)
    sku_name = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.sku_name


class Visit(models.Model):
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE, null=True, related_name='Территория')
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE, related_name='Магазин')
    sku = models.ManyToManyField(Sku, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment=models.TextField(null=True)
    visit_date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.trade} {self.visit_date}'