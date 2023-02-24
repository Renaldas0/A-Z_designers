from django.db import models
from django.contrib.auth.models import User


class DiscountCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    valid_for_first_purchase = models.BooleanField(default=True)
    discount_percentage = models.IntegerField(default=10)

    def apply_discount(self, user):
        if self.valid_for_first_purchase:
            if user.orders.count() == 0:
                return self.discount_percentage
        else:
            return self.discount_percentage

    def __str__(self):
        return self.code
