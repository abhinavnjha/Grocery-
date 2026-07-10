from .cart import Cart


def cart(request):
    return {"nav_cart": Cart(request)}
