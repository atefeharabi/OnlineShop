from django.contrib import admin
from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date', 'payment_status', 'order_status', 'total_amount')
    ordering = ('order_date', 'customer')
    list_filter = ('order_status', 'payment_status')
    search_fields = ('customer',)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'number_of_order', 'order')
    ordering = ('product', )
    list_filter = ('order', )
    search_fields = ('product',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
