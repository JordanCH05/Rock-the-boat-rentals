from django.urls import path
from . import views

urlpatterns = [
    path('add/<sku>', views.add_review, name='add_review'),
]
