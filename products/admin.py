from django.contrib import admin
from .models import Product, Category, Discount, Feature


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('name', 'sub_category', 'is_sub')
    ordering = ('name', 'sub_category')
    list_filter = ('is_sub',)
    search_fields = ('name', 'sub_category')


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('manufacturer', 'name')}
    list_display = ('slug', 'category', 'price', 'stock', 'available', 'created', 'rate', 'vote')
    ordering = ('slug', 'category', 'price')
    list_filter = ('available', 'discount')
    search_fields = ('name', 'category', 'manufacturer')


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('discount_type', 'percent', 'amount', 'max_amount', 'coupon', 'coupon_used')
    ordering = ('discount_type',)
    list_filter = ('percent', 'amount', 'coupon')
    search_fields = ('percent', 'amount', 'coupon')


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'description')
    ordering = ('product', 'name')
    list_filter = ('product',)
    search_fields = ('product',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Feature, FeatureAdmin)
