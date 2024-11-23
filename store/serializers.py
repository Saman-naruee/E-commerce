from .models import Product, Review, Promotion
from category.models import Category
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    collection = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = serializers.StringRelatedField()

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
            'price_with_tax',
        ]
        read_only_fields = [
            'id',
            'last_updated',
        ]
    def calculate_tax(self, product: Product):
        return product.price * float(1.09)
