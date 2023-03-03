from django.urls import path
from .views import Cart, CartAdd, CartRemove, CartUpdate, OrderCreate, OrderDetail, OrderPay

app_name = 'orders'
urlpatterns = [
    path('create/', OrderCreate.as_view(), name='order-create'),
    path('detail/<int:order_id>/', OrderDetail.as_view(), name='order-detail'),
    path('cart/', Cart.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', CartAdd.as_view(), name='cart-add'),
    path('cart/remove/<int:product_id>/', CartRemove.as_view(), name='cart-remove'),
    path('cart/update/<int:product_id>/', CartUpdate.as_view(), name='cart-update'),
    path('pay/<int:order_id>/', OrderPay.as_view(), name='order-pay'),
]