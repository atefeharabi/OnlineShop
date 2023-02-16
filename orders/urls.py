from django.urls import path
from .views import Cart

app_name = 'orders'
urlpatterns = [
    path('cart', Cart.as_view(), name='cart')
]