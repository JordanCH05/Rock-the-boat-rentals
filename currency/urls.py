from django.urls import path
from . import views


urlpatterns = [
    path('<currency>/', views.change_currency, name='change_currency'),
    path(
        '<currency>/<path:redirect_url>/',
        views.change_currency,
        name='change_currency'
        ),
]
