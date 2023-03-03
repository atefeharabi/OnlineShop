from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .cart import CartSession
from products.models import Product
from orders.forms import CartAddForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import OrderItem, Order


class Cart(View):
    """
    View shopping cart
    """
    template_name = 'orders/cart.html'

    def get(self, request):
        cart = CartSession(request)
        return render(request, self.template_name, {'cart': cart})


class CartAdd(View):
    """
    Adding the desired number of products to the cart
    """
    def post(self, request, product_id):
        cart_session = CartSession(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddForm(request.POST)
        # if form.cleaned_data['quantity'] > product.stock:
        #     messages.error(request, 'Quantity is more than stock', 'danger')
        #     return redirect('products:product-detail')
        if form.is_valid():
            cart_session.add(product, form.cleaned_data['quantity'])
        return redirect('products:product-detail', slug=product.slug)


class CartRemove(View):
    """
    Removing an item from shopping cart
    """
    def get(self, request, product_id):
        cart_session = CartSession(request)
        product = get_object_or_404(Product, id=product_id)
        cart_session.remove(product)
        return redirect('orders:cart')


class CartUpdate(View):
    """
    Updating products quantity from shopping cart
    """
    def get(self, request, product_id):
        cart_session = CartSession(request)
        product = get_object_or_404(Product, id=product_id)
        new_quantity = int(request.GET['q'])
        cart_session.update(product, new_quantity)
        return redirect('orders:cart')


class OrderCreate(LoginRequiredMixin, View):
    def get(self, request):
        cart_session = CartSession(request)
        order = Order.objects.create(customer=request.user)
        for item in cart_session:
            OrderItem.objects.create(order=order, product=item['product'], price=item['final_price'],
                                     quantity=item['quantity'])
        cart_session.clear()
        return redirect('orders:order-detail', order.id)


class OrderDetail(LoginRequiredMixin, View):
    template_name = 'orders/order.html'

    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return render(request, self.template_name, {'order': order})


class OrderPay(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        order.payment_status = order.PAYMENT[0][0]
        order.save()
        messages.success(request, 'Payment was successful. Please refer to your user panel to view the status of your order',
                         'success')
        return redirect('products:home')
