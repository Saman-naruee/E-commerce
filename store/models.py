from django.db import models
from category.models import Category

class Product(models.Model):  
    title = models.CharField(max_length=200)  
    slug = models.SlugField(max_length=200)  
    price = models.PositiveBigIntegerField()  
    inventory = models.PositiveBigIntegerField()  
    category = models.ForeignKey('category.Category', on_delete=models.PROTECT, related_name='products')  
    last_updated = models.DateTimeField(auto_now=True)  
    description = models.TextField()  
    image = models.FileField(upload_to='media/images/')  

    def __str__(self) -> str:  
        return self.title  

    class Meta:  
        ordering = ['title']  
    
class Promotion(models.Model):
    description = models.CharField(max_length=255, default='')
    discount = models.FloatField(default=0)

    def __str__(self) -> str:
        return str(self.discount)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reveiws')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
