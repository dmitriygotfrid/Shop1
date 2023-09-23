from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from .views import IndexView, ProductsListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('products/category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('products/page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('products/baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('products/baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
]
