from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=500)


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)    
    address = models.CharField(max_length=1000)
    address2 = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=10, default='00000')
    total = models.CharField(max_length=200)
    ccname = models.CharField(max_length=200, default='')
    ccnumber = models.CharField(max_length=16, default='')  
    expiration = models.CharField(max_length=10, default='')  
    cvv = models.CharField(max_length=4, default='') 