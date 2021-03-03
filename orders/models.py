from django.db import models
from django.utils.translation import gettext as _

from products.models import Product
from tables.models import Table

ORDER_STATUS = (
    ('crt', _('Created')),
    ('wrk', _('In work')),
    ('cls', _('Closed')),
    ('paid', _('Paid')),
)

UNIT_STATUS = (
    ('wait', _('Wait')),
    ('cnl', _('Cancel')),
    ('dlvrd', _('Delivered')),
)


class OrderUnit(models.Model):
    '''Model description unit product for order in basket.'''

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        blank=True, null=True, verbose_name=_('Product')
        )

    value = models.IntegerField(_('Value of Order Unit'))

    status = models.CharField(
        verbose_name=_('Status'),
        max_length=25, choices=UNIT_STATUS
        )

    def __str__(self):
        return f'id:{self.id} {self.product}x{self.value}'

    class Meta:
        verbose_name = 'Order Unit'
        verbose_name_plural = 'Order Units'


class Order(models.Model):
    '''Model description order.'''

    products = models.ManyToManyField(
        OrderUnit, default=None,
        verbose_name=_('Products')
        )

    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Time created order')
    )

    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Time updated order')
    )

    status = models.CharField(
        verbose_name=_('Status'),
        max_length=25, choices=ORDER_STATUS
        )

    table = models.ForeignKey(
        Table, on_delete=models.SET_NULL,
        null=True, verbose_name=_('Table'))

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
