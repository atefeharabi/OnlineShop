from django import forms
from django.core.exceptions import ValidationError


class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=10)

    def check_quantity(self, stock):
        if self.quantity > stock:
            raise ValidationError('Quantity is over than stock')
        return True

