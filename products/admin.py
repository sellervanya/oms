from django.contrib import admin

from .models import Category, SubCategory, Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('pk', 'name', 'subcategory', 'get_category',)
    list_filter = ('subcategory',)


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product, ProductAdmin)
