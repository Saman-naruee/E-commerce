from django.db import models
from store.models import Product
from user.models import UserProfile

class Order(models.Model):
    class PaymentStatus(models.TextChoices):
        PENDING = 'P', 'Pending'
        COMPLETE = 'C', 'Complete'
        FAILED = 'F', 'Failed'

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PaymentStatus, default=PaymentStatus.PENDING)
    UserProfile = models.ForeignKey(UserProfile, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{UserProfile.user.first_name} order : {self.payment_status}'
    
    class Meta:
        permissions = [
            ('cancel_order', 'Can cancel orders')
        ]
 
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveBigIntegerField()
