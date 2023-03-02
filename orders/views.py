from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .cart import CartSession
from products.models import Product
from orders.forms import CartAddForm
from django.contrib import messages


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

