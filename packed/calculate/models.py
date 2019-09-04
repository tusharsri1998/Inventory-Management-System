from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    p_id = models.CharField(max_length=10, primary_key=True)
    p_name = models.CharField(max_length=30)
    box_type_name = models.CharField(max_length = 20, null = True)
    box_type=models.IntegerField(null = True)
    one_pc_weight = models.FloatField(null = True)
    box_weight = models.FloatField(null = True)
    box_size_1 = models.CharField(max_length=20, null = True)
    box_size_2 = models.CharField(max_length=20, null = True)


class Box(models.Model):
    sku=models.ForeignKey(Product,related_name='product',on_delete=models.CASCADE)
    quantity=models.IntegerField()


class invoice(models.Model):
    entry_date = models.DateField()
    invoice_number=models.IntegerField()
