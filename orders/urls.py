from django.urls import path
from .views import Cart, CartAdd

app_name = 'orders'
urlpatterns = [
    path('cart', Cart.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', CartAdd.as_view(), name='cart-add'),
]