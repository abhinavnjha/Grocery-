from decimal import Decimal
from .models import Product

CART_SESSION_KEY = "cart"


class Cart:
    """Simple session-based cart. No login required, so anyone can shop right away."""

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_KEY)
        if cart is None:
            cart = self.session[CART_SESSION_KEY] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]["quantity"] += quantity
        else:
            self.cart[product_id] = {"quantity": quantity}
        self.save()

    def set_quantity(self, product, quantity):
        product_id = str(product.id)
        if quantity <= 0:
            self.remove(product)
            return
        self.cart[product_id] = {"quantity": quantity}
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session[CART_SESSION_KEY] = self.cart
        self.session.modified = True

    def clear(self):
        self.session[CART_SESSION_KEY] = {}
        self.session.modified = True

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        products_map = {str(p.id): p for p in products}
        for product_id, item in self.cart.items():
            product = products_map.get(product_id)
            if not product:
                continue
            quantity = item["quantity"]
            yield {
                "product": product,
                "quantity": quantity,
                "subtotal": product.price * quantity,
            }

    def get_total(self):
        return sum(item["subtotal"] for item in self)
