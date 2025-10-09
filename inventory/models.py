from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.category
    
class Product(models.Model):
    product_name = models.CharField(max_length=150)
    product_category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='products')
    product_price = models.DecimalField(max_digits=10,decimal_places=2)
    product_qty = models.IntegerField(default=0)
    min_qty = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product_name}'
    
    @property
    def is_low_stock(self):
        return self.product_qty <= self.min_qty
    

class StockTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('IN','Stock In'),
        ("OUT",'Stock Out'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    transaction_qty = models.IntegerField()
    notes = models.TextField(blank=True)

