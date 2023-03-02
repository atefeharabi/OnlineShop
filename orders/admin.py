from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date', 'payment_status', 'order_status', 'updated')
    ordering = ('order_date', 'customer')
    list_filter = ('order_status', 'payment_status')
    search_fields = ('customer',)
    inlines = (OrderItemInline,)


# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ('product', 'order', 'price', 'quantity')
#     ordering = ('product', )
#     list_filter = ('order', )
#     search_fields = ('product',)


# admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem, OrderItemAdmin)
