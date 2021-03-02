from django.db import models
from django.utils.translation import gettext as _

from products.models import Drink, Dish

ORDER_STATUS = (
    ('crt', 'created'),
    ('wrk', 'in work'),
    ('cls', 'closed'),
    ('paid', 'paid'),
)


class MenuPosition(models.Model):
    '''Model description tempary product in basket.'''

    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, blank=True, null=True)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Position'


class Order(models.Model):
    '''Model description tempary product in basket.'''

    products = models.ManyToManyField(MenuPosition, default=None)
    status = models.CharField(max_length=25, choices=ORDER_STATUS)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Order'
