from django.views.generic import DetailView, ListView

from .models import Product, SubCategory


class SubCategoryView(ListView):
    '''Model description view for index page'''
    model = SubCategory
    template_name = 'index.html'
    context_object_name = 'subcategories'


class ProductDetailView(DetailView):
    '''Model description detail view product'''
    model = Product


class ListProductByCategory(ListView):
    paginate_by = 4
    model = Product

    def get_queryset(self):
        model = self.model
        category = self.kwargs['cat']
        result = model.objects.filter(subcategory__category__pk=category)
        if 'subcat' in self.kwargs.keys():
            subcategory = self.kwargs['subcat']
            return result.filter(subcategory__pk=subcategory)
        return result
