from django.db import models


class character(models.Model):
    character_id = models.AutoField(primary_key = True)
    character_name = models.CharField(max_length = 20)
    character_price = models.IntegerField()
    character_quantity = models.IntegerField()
    character_date = models.DateField()


class sales(models.Model):
    sales_id = models.AutoField(primary_key = True)
    sales_name = models.CharField(max_length = 20)
    sales_price = models.IntegerField()
    sales_quantity = models.IntegerField()
    sales_date = models.DateField()


class stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    stock_name = models.CharField(max_length=20)
    stock_price = models.IntegerField()
    stock_quantity = models.IntegerField()
    stock_date = models.DateField()



