from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('', views.CategoryViewSet.as_view(), name='category-list'),
    path('<int:pk>/', views.CategoryViewSet.as_view(), name='category-detail'),
]
