from django.urls import path
from .views import ProductView, home

app_name = 'store'

urlpatterns = [
    path('', ProductView.as_view(), name='products'),
    path('<int:product_id>', ProductView.as_view(), name='product')
]
