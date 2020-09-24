from django.db import models
from currency.models import Currency


class Rate(models.Model):
    rate = models.DecimalField('Rate', max_digits=20, decimal_places=6)
    date = models.DateField('Date')
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="rates")

    class Meta:
        ordering = ['-date']
        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'
