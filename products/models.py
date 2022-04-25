from django.db import models
from currencies.models import Currency
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

    sku = models.CharField(max_length=10, unique=True, default='test')
    price = models.DecimalField(max_digits=8, decimal_places=2)
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
    views = models.IntegerField(default=0, null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True)
    currency = models.ForeignKey(
        Currency, default='EUR', on_delete=models.SET_DEFAULT,
        null=True, blank=True, max_length=3,
        )

    class Meta:
        ordering = ['-image', '-views']

    def __str__(self):
        return str(self.sku)
