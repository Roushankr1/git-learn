# Generated by Django 4.2.13 on 2024-06-17 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='character',
            fields=[
                ('character_id', models.AutoField(primary_key=True, serialize=False)),
                ('character_name', models.CharField(max_length=20)),
                ('character_price', models.IntegerField()),
                ('character_quantity', models.IntegerField()),
                ('character_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='sales',
            fields=[
                ('sales_id', models.AutoField(primary_key=True, serialize=False)),
                ('sales_name', models.CharField(max_length=20)),
                ('sales_price', models.IntegerField()),
                ('sales_quantity', models.IntegerField()),
                ('sales_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='stock',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False)),
                ('stock_name', models.CharField(max_length=20)),
                ('stock_price', models.IntegerField()),
                ('stock_quantity', models.IntegerField()),
                ('stock_date', models.DateField()),
            ],
        ),
    ]