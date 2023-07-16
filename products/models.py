from django.db import models


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

    def __str__(self):
        return self.name