from django.db import models


class Currency(models.Model):
    name = models.CharField('Currency name', max_length=255)
    code = models.CharField('Currency code', max_length=3)
    is_base = models.BooleanField('Is base currency?', default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'


