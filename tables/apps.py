from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TablesConfig(AppConfig):
    name = 'tables'
    verbose_name = _('OrdersTable')
