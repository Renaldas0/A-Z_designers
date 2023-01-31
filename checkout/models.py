import uuid


from django.db import models
from django.db.models import Sun
from django.conf import settings

from products.models import Product


class Order(models.Model):

    order_number = models.CharField(max_length=32, editable=False, null=False)
    full_name = models.CharField(max_length=64, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    country = models.CharField(max_length=36, null=False, blank=False)
    city = models.CharField(max_length=36, null=False, blank=False)
    address = models.CharField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    product_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)


class OrderLineItem(models.Model):

    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)  # XS, S, M, L, XL
    shoe_size = models.CharField(max_length=2, null=True, blank=True)  # 37, 38, 39, 40, 41
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
