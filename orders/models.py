from django.db import models
from products.models import Product
from customers.models import Customer


class Order(models.Model):
    PAYMENT = [('PA', 'Paid'), ('UP', 'Unpaid')]
    ORDER_STATUS = [('C', 'Confirmed'), ('D', 'Delivered'), ('P', 'Processed')]
    order_date = models.DateField(auto_now_add=True)
    amount = models.FloatField()
    payment_status = models.CharField(choices=PAYMENT, max_length=2)
    order_status = models.CharField(choices=ORDER_STATUS, max_length=1)
    use_discount = models.BooleanField()
    total_amount = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)






