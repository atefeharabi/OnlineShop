from django.urls import path
from .views import Cart, CartAdd, CartRemove, CartUpdate

app_name = 'orders'
urlpatterns = [
    path('cart', Cart.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', CartAdd.as_view(), name='cart-add'),
    path('cart/remove/<int:product_id>/', CartRemove.as_view(), name='cart-remove'),
    path('cart/update/<int:product_id>/', CartUpdate.as_view(), name='cart-update'),
]