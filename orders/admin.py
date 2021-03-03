from django.contrib import admin

from .models import OrderUnit, Order


class OrderUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'status')
    list_filter = ('status',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'table')


admin.site.register(OrderUnit, OrderUnitAdmin)
admin.site.register(Order, OrderAdmin)
