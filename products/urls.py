from django.urls import path
from .views import Home, ProductDetail, CategoryDetail

app_name = 'products'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<slug:slug>/', Home.as_view(), name='category-detail'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product-detail'),
]