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



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount)
admin.site.register(Feature)
