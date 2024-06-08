from django.db import models

class product(models.Model):
    product_id = models.AutoField(primary_key = True)
    product_name = models.CharField(max_length = 20)
    product_prize = models.IntegerField()
    product_quantity = models.IntegerField()
    product_date = models.DateField()

class sales(models.Model):
    sales_id = models.AutoField(primary_key = True)
    sales_name = models.CharField(max_length = 20)
    sales_prize = models.IntegerField()
    sales_quantity = models.IntegerField()
    sales_date = models.DateField()

class stock(models.Model):
    stock_id = models.AutoField(primary_key = True)
    stock_name = models.CharField(max_length = 20)
    stock_prize = models.IntegerField()
    stock_quantity = models.IntegerField()
    stock_date = models.DateField()
    stock_expiry = models.DateField()







# Create your models here.
