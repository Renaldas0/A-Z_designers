from django.db import models
from products.models import Product, Category
from django.contrib.auth.models import User


class Review(models.Model):
    # Model for logged in users to leave a review
    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES, default=3)
    review = models.TextField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Meta class for Review model """
        ordering = ['-date']

    def __str__(self):
        return self.review
