from django.urls import path

from .views import SubCategoryView, ProductDetailView, ListProductByCategory

urlpatterns = [
    path('', SubCategoryView.as_view(), name='products'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='view_detail_product'),
    path('cat/<int:cat>', ListProductByCategory.as_view(), name='prod_by_cat'),
    path('cat/<int:cat>/<int:subcat>', ListProductByCategory.as_view(), name='prod_by_subcat')
]
