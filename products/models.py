from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):

    class Meta:
        verbose_name = 'Categories'
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Brand(models.Model):

    class Meta:
        verbose_name = 'Product Brand'
    name = models.CharField(max_length= 250)

    def __str__(self):
        return self.name


class League(models.Model):

    class Meta:
        verbose_name = "Product's League"
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


CLOTHING_SIZES = (
    ("XS", "XS"),
    ("S", "S"),
    ("M", "M"),
    ("L", "L"),
    ("XL", "XL"),
)


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    league = models.ForeignKey(League, null=True, blank=True, on_delete=models.SET_NULL, default='unknown')
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL, default='unknown')
    sku = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250)
    desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='media/products')
    size = models.CharField(max_length=20, choices=CLOTHING_SIZES, default="M")

    def __str__(self):
        return self.name


class SavedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')
