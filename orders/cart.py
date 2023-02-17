from products.models import Product

CART_SESSION_ID = 'cart'


class CartSession:
    def __init__(self, request):
        self.session = request.session
        print(self.session)
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            self.session[CART_SESSION_ID]={}
        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product.name

        for item in cart.values():
            item['total_price'] = int(item['final_price']) * item['quantity']
            yield item

    def __len__(self):
        if self.cart.values():
            return sum(item['quantity'] for item in self.cart.values())
        return 0

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0, 'price': str(product.price), 'final_price': str(product.price)
            }
        self.cart[product_id]['quantity'] += quantity
        if product.discount:
            self.cart[product_id]['final_price'] = product.final_price
        self.session.modified = True

