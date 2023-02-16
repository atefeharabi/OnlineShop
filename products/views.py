from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Category, Feature
from orders.forms import CartAddForm


class Home(View):
    template_name = 'products/home.html'

    def get(self, request, slug=None):
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)
        if slug:
            category = Category.objects.get(slug=slug)
            products = products.filter(category=category)
            categories = Category.objects.filter(sub_category=category)
        render(request, 'inc/navbar.html', {'categories': categories})
        return render(request, self.template_name, {'products': products, 'categories': categories})


class ProductDetail(View):
    template_name = 'products/detail.html'

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        features = Feature.objects.filter(product=product.id)
        form = CartAddForm()
        return render(request, self.template_name, {'product': product, 'features': features, 'form': form})


class CategoryDetail(View):
    pass