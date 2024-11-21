from .models import Product, Review, Promotion
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'price',
            'inventory',
            'category',
            'last_updated',
            'description',
            'image',
        ]
        read_only_fields = [
            'id',
            'last_updated',
        ]
