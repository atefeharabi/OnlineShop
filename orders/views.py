from django.shortcuts import render
from django.views import View


class Cart(View):
    def get(self, request):
        return render(request, 'orders/cart.html')