from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return self.friendly_name


class Boat(models.Model):

    sku = models.CharField(max_length=10, unique=True, null=True, blank=True)
    currency = models.CharField(max_length=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category, blank=True)
    manufacturer = models.CharField(max_length=254, null=True, blank=True)
    condition = models.CharField(max_length=254, null=True, blank=True)
    fuel = models.CharField(max_length=254, null=True, blank=True)
    year_built = models.IntegerField(null=True, blank=True)
    length = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    width = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    material = models.CharField(max_length=254, null=True, blank=True)
    location = models.CharField(max_length=254, null=True, blank=True)
    number_of_views = models.IntegerField(null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True)

    class Meta:
        ordering = ['-image', '-number_of_views']

    def __str__(self):
        return str(self.sku)
