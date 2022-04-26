from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<boat_id>/', views.add_to_bag, name='add_to_bag'),
    path('remove/<boat_id>/', views.remove_from_bag, name='remove_from_bag'),
]
