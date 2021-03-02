from django.db import models
from django.utils.translation import gettext as _
from django.shortcuts import reverse


UNIT_OF_MEAUSEREMENT = (
    ('KG', _('killogramm')),
    ('GR', _('gramm')),
    ('ML', _('mill')),
    ('L', _('liter')),
)


class Category(models.Model):
    '''Model description of the category products.'''
    name = models.CharField(
        _('Name'), max_length=55,
        unique=True, blank=False
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class SubCategory(models.Model):
    '''Model description of the category products.'''

    name = models.CharField(
        _('Name'), max_length=55,
        unique=True, blank=False
        )

    category = models.ForeignKey(
        Category, verbose_name=_('Category'),
        on_delelte=models.SET_NULL, null=True
        )

    alcohol = models.IntegerField(
        verbose_name=_('Alcohol percent'), default=False
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('SubCategory')
        verbose_name_plural = _('SubCategories')


class Product(models.Model):
    '''Model description of the alco/noalco drink.'''
    name = models.CharField(
        _('Name'), max_length=55,
        unique=True, blank=False
        )

    description = models.CharField(_('Description'), max_length=500)
    subcategory = models.ForeignKey(SubCategory, models.SET_NULL, null=True)
    volume = models.IntegerField(_('Volume'))
    measurement = models.CharField(choices=UNIT_OF_MEAUSEREMENT, max_length=25)
    calories = models.IntegerField(_('Calories'))
    image = models.ImageField(_('Image'), default='None.jpg')

    def get_absolute_url(self):
        return reverse("product", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
