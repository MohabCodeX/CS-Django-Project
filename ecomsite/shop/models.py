from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=500)