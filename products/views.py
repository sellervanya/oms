from django.views.generic import DetailView, ListView

from .models import Drink, Dish, DrinkCategory, DishCategory


class ProductsView(ListView):
    model = DishCategory
    template_name = 'index.html'
    context_object_name = 'dish_cat'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['drink_cat'] = DrinkCategory.objects.all()
        return context


class DetailDrinkView(DetailView):
    model = Drink


class DetailDishView(DetailView):
    model = Dish


class ListViewDrinks(ListView):
    model = Drink
    paginate_by = 4


class ListViewDishes(ListView):
    model = Dish
    paginate_by = 4


class ListByCategory(ListView):
    paginate_by = 4

    models_dict = {
        'drinks': Drink,
        'dishes': Dish
    }

    def get_queryset(self):
        kwargs_model = self.kwargs['model']
        model = self.models_dict[kwargs_model]
        cat = self.kwargs['cat']
        return model.objects.filter(category__pk=cat)
