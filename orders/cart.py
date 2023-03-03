from products.models import Product
from decimal import Decimal

CART_SESSION_ID = 'cart'
ZERO = 0


class CartSession:

    def __init__(self, request):
        """
        Preparing the shopping cart session
        :param request:
        """
        self.session = request.session
        if not self.session.get(CART_SESSION_ID):
            cart = self.session[CART_SESSION_ID] = {}
        else:
            cart = self.session.get(CART_SESSION_ID)
        self.cart = cart

    def __iter__(self):
        """
        Make an iterable object from shopping cart session
        :return:
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
            cart[str(product.id)]['id'] = product.id

        for item in cart.values():
            item['total_price'] = Decimal(item['final_price']) * item['quantity']
            yield item

    def __len__(self):
        """
        Calculating the number of orders in shopping cart
        :return:
        """
        if self.cart.values():
            return sum(item['quantity'] for item in self.cart.values())
        return 0

    def add(self, product, quantity):
        """
        Adding desired number of products to shopping cart session
        :param product:
        :param quantity:
        :return:
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': ZERO, 'price': str(product.price), 'final_price': str(product.price)
            }
        self.cart[product_id]['quantity'] = int(self.cart[product_id]['quantity']) + quantity
        if product.discount:
            self.cart[product_id]['final_price'] = str(product.final_price)
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def update(self, product, new_quantity):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] = new_quantity
            # self.total_price()
            self.session.modified = True

    def total_price(self):
        """
        Calculating total price for an order
        :return:
        """
        return sum(Decimal(item['final_price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.session.modified = True