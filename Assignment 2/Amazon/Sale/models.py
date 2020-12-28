from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.IntegerField()
    gender = models.CharField(max_length=100, default='')

class Shop(models.Model):
    shop_name = models.CharField(max_length=100)
    contact = models.IntegerField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default='')
    contact_person = models.CharField(max_length=255)
    branded = models.CharField(max_length=100, default='')
    email = models.EmailField()

class Product(models.Model):
    Shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='test.jpg',null=True, upload_to='shop')
    product_name = models.CharField(max_length=200, default='')
    price = models.CharField(max_length=200, default='')
    discount = models.IntegerField()
    old_price = models.CharField(max_length=200, default='')
    is_approve = models.BooleanField(blank=True, default=False)

class Deals(models.Model):
    Shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    deal_name = models.CharField(max_length=200, default='')
    valid_from = models.DateTimeField()
    valid_till = models.DateTimeField()
    discount_per = models.CharField(max_length=200, default='')
    is_approve = models.BooleanField(blank=True, default=False)
