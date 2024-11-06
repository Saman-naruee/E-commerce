from django.contrib import admin  
from django.urls import reverse  
from django.utils.html import format_html, urlencode  
from django.db.models import Count  
from django.db.models.query import QuerySet  
from django.http import HttpRequest  
from .models import Category  
from typing import Any  

@admin.register(Category)  
class CategoryAdmin(admin.ModelAdmin):  
    list_display = ['name', 'product_count']  # Changed from 'title' to 'name'  
    list_per_page = 20  
    search_fields = ['name']  # Changed from 'title' to 'name'  

    @admin.display(ordering='product_count')  
    def product_count(self, obj):  # Use `obj` instead of `Category`  
        related_url = reverse('admin:store_product_changelist') + '?' + urlencode({  
            'category_id': str(obj.pk)  # Use the passed object to get the primary key  
        })  
        return format_html(f'<a href="{related_url}">{obj.product_count}</a>')  # Access using `obj`  

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:  
        return super().get_queryset(request).annotate(  
            product_count=Count('products')  
        )
