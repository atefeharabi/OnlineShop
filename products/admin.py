from django.contrib import admin
from .models import Product, Category, Discount, Feature

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount)
admin.site.register(Feature)
