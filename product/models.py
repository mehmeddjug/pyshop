from django.db import models
from datetime import datetime


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=datetime.now)
    on_sale = models.BooleanField(default=False)
    discount = models.CharField(max_length=3)