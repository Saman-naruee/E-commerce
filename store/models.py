from django.db import models
from category.models import Category

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    price = models.PositiveBigIntegerField()
    inventory = models.PositiveBigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    last_updated = models.DateTimeField(auto_now=True)
    description = models.TextField()
    image = models.FileField(upload_to='media/images/')
