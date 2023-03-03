from django.db import models
from products.models import Product
from accounts.models import User


class Order(models.Model):
    PAYMENT = [('PA', 'Paid'), ('UP', 'Unpaid')]
    ORDER_STATUS = [('C', 'Confirmed'), ('D', 'Delivered'), ('P', 'Processed')]
    order_date = models.DateField(auto_now_add=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_status = models.CharField(choices=PAYMENT, max_length=2, default=PAYMENT[1][0])
    order_status = models.CharField(choices=ORDER_STATUS, max_length=1, default=ORDER_STATUS[2][0])
    use_discount = models.BooleanField(default=False)
    # price_after_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ('payment_status', 'updated')

    def __str__(self):
        return f"{self.customer} - {str(self.id)}"

    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())

    def after_discount(self):
        pass


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity






