from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Category, Feature


class Home(View):
    template_name = 'products/home.html'

    def get(self, request):
        products = Product.objects.filter(available=True)
        categories = Category.objects.all()
        return render(request, self.template_name, {'products': products, 'categories': categories})


class ProductDetail(View):
    template_name = 'products/detail.html'

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        features = Feature.objects.filter(product=product.id)
        return render(request, self.template_name, {'product': product, 'features': features})


class CategoryDetail(View):
    pass