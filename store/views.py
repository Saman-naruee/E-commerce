from django.shortcuts import render
from  .models import Product, Review, Promotion
from .serializers import ProductSerializer
from rest_framework.views import APIView, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser, AllowAny 
from rest_framework.response import Response


class ProductView(APIView):
    queryset = Product.objects.all()

    def get_permissions(self):
        if self.request.method in ['DELETE']:
            return [IsAdminUser()]
        return [AllowAny()]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, product_id):
        if product_id:
            product = Product.objects.get(id=product_id)
            serializer = ProductSerializer(product, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, product_id):
        if product_id:
            product = Product.objects.get(id=product_id)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        

@api_view(['GET'])
def home(request):
    data = {
        "message":"Welcome to our E-commerce API!"
    }
    return Response(data, status=status.HTTP_200_OK)
