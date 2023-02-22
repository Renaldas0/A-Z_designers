from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    gender = models.CharField(max_length=24, null=True)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __gen__(self):
        return self.gender

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    key_words = models.TextField(blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    colour = models.CharField(max_length=24, null=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    materials = models.CharField(max_length=254, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """return product name by default"""
        return self.name

    def review_count(self):
        """Return total reviews for product"""
        count = self.reviews.aggregate(
            count=models.Count('rating'))['count']

        if count is None:
            count = 0

        return count


class Review(models.Model):
    # Model for customers to leave a review
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES, default=3)
    review = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review
