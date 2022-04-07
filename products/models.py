from django.db import models


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

    currency = models.CharField(max_length=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category, blank=True)
    manufacturer = models.CharField(max_length=254, null=True, blank=True)
    condition = models.CharField(max_length=254, null=True, blank=True)
    fuel = models.CharField(max_length=254, null=True, blank=True)
    year_built = models.IntegerField(null=True, blank=True)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    material = models.CharField(max_length=254, null=True, blank=True)
    location = models.CharField(max_length=254, null=True, blank=True)
    number_of_views_last_7_days = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.pk
