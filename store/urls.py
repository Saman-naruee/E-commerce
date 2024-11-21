from django.urls import path
from .views import ProductView, home

app_name = 'store'

urlpatterns = [
    path('', home, name='home'),
    path('products/', ProductView.as_view(), name='products'),
    path('products/<int:product_id>', ProductView.as_view(), name='product')
]
