from django.urls import path

from . views import ProductsView, DetailDishView, DetailDrinkView,\
    ListViewDrinks, ListViewDishes, ListByCategory


urlpatterns = [
    path('', ProductsView.as_view(), name='products'),
    path('dish/<int:pk>', DetailDishView.as_view(), name='view_detail_dish'),
    path('drink/<int:pk>', DetailDrinkView.as_view(), name='view_detail_drink'),
    path('drinks', ListViewDrinks.as_view(), name='list_drinks'),
    path('dishes', ListViewDishes.as_view(), name='list_dishes'),
    path('<str:model>/cat/<int:cat>', ListByCategory.as_view(), name='prod_by_cat')
]
