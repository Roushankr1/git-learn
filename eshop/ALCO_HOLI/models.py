from django.db import models

class instrument(models.Model):
    instrument_id = models.AutoField(primary_key = True)
    instrument_name = models.CharField(max_length = 20)
    instrument_prize = models.IntegerField()
    instrument_quantity = models.IntegerField()
    instrument_date = models.DateField()

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