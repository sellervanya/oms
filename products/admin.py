from django.contrib import admin
from .models import Dish, DishCategory, Drink, DrinkCategory

admin.site.register(Dish)
admin.site.register(DishCategory)
admin.site.register(Drink)
admin.site.register(DrinkCategory)
