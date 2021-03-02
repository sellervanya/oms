from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Table(models.Model):
    '''Model description table for order'''
    table_num = models.IntegerField(
        primary_key=True, unique=True, auto_created=True,
        verbose_name=_('TableNumber')
        )

    user_foreign = models.OneToOneField(
        User, on_delete=models.CASCADE,
        verbose_name=_('UserRecordForTable')
        )

    def __str__(self):
        return str(self.table_num)

    class Meta:
        verbose_name = _('Table')
        verbose_name_plural = _('Tables')
