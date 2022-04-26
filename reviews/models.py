from django.db import models
from django.contrib.auth.models import User

from products.models import Boat


class Review(models.Model):
    """ Boat Review Model """
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    boat = models.ForeignKey(
        Boat, on_delete=models.CASCADE, related_name='reviews')
    score = models.DecimalField(decimal_places=1, max_digits=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Review of {self.boat} by {self.username}'
