from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):  
    name = models.CharField(max_length=200)  
    slug = models.SlugField(max_length=200)  
    description = models.TextField()  
    featured_product = models.ForeignKey(  
        'store.Product',  # Reference to the Product model in another app  
        on_delete=models.SET_NULL,  
        null=True,  
        related_name='featured_categories',  
        blank=True  
    )  
    parent = TreeForeignKey(  
        'self',  
        on_delete=models.CASCADE,  
        null=True,  
        blank=True,  
        related_name='children'  
    )  

    def __str__(self):  
        return self.name 
