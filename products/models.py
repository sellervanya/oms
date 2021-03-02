from django.db import models
from django.utils.translation import gettext as _
from django.shortcuts import reverse


UNIT_OF_MEAUSEREMENT = (
    ('KG', _('killogramm')),
    ('GR', _('gramm')),
    ('ML', _('mill')),
    ('L', _('liter')),
)


class DrinkCategory(models.Model):
    '''Model description of the category drinks.'''
    name = models.CharField(
        _('Name'), max_length=55,
        unique=True, blank=False
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('DrinkCategory')
        verbose_name_plural = _('DrinkCategorys')


class DishCategory(models.Model):
    '''Model description of the category dishes.'''
    name = models.CharField(
        _('Name'), max_length=55,
        unique=True, blank=False
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('DishCategory')
        verbose_name_plural = _('DishCategorys')


class Drink(models.Model):
    '''Model description of the alco/noalco drink.'''
    name = models.CharField(
        _('Name'), max_length=55,
        unique=True, blank=False
        )

    description = models.CharField(_('Description'), max_length=500)
    category = models.ForeignKey(DrinkCategory, models.SET_NULL, null=True)
    volume = models.IntegerField(_('Volume'))
    measurement = models.CharField(choices=UNIT_OF_MEAUSEREMENT, max_length=25)
    calories = models.IntegerField(_('Calories'))
    image = models.ImageField(_('Image'), default='None.jpg')
    alcohol = models.BooleanField(verbose_name=_('isAlcohol'), default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Drink')
        verbose_name_plural = _('Drinks')


class Dish(models.Model):
    '''Model description of the dishes.'''
    name = models.CharField(
        _('Name'), max_length=55,
        unique=True, blank=False
        )

    description = models.CharField(_('Description'), max_length=500)
    category = models.ForeignKey(
        DishCategory, models.SET_NULL, null=True
        )

    volume = models.IntegerField(_('Volume'))
    measurement = models.CharField(choices=UNIT_OF_MEAUSEREMENT, max_length=25)
    calories = models.IntegerField(_('Calories'))
    image = models.ImageField(_('Image'), default='None.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detaildish", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = _('Dish')
        verbose_name_plural = _('Dishes')
