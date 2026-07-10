from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .cart import Cart
from .models import Category, Product, Order, OrderItem


def home(request):
    categories = Category.objects.all()
    featured = Product.objects.filter(is_featured=True)[:8]
    new_arrivals = Product.objects.order_by("-created_at")[:8]
    return render(request, "store/home.html", {
        "categories": categories,
        "featured": featured,
        "new_arrivals": new_arrivals,
    })


def shop(request):
    products = Product.objects.select_related("category").all()
    categories = Category.objects.all()

    query = request.GET.get("q", "").strip()
    category_slug = request.GET.get("category", "")
    sort = request.GET.get("sort", "")

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    if category_slug:
        products = products.filter(category__slug=category_slug)

    if sort == "price_low":
        products = products.order_by("price")
    elif sort == "price_high":
        products = products.order_by("-price")
    elif sort == "name":
        products = products.order_by("name")

    return render(request, "store/shop.html", {
        "products": products,
        "categories": categories,
        "query": query,
        "active_category": category_slug,
        "sort": sort,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    return render(request, "store/product_detail.html", {
        "product": product,
        "related": related,
    })


@require_POST
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    quantity = int(request.POST.get("quantity", 1))
    cart.add(product, quantity)
    messages.success(request, f"Added {product.name} to your basket.")
    next_url = request.POST.get("next") or "shop"
    return redirect(next_url)


@require_POST
def cart_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    quantity = int(request.POST.get("quantity", 1))
    cart.set_quantity(product, quantity)
    return redirect("cart_detail")


@require_POST
def cart_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.remove(product)
    messages.info(request, f"Removed {product.name} from your basket.")
    return redirect("cart_detail")


def cart_detail(request):
    cart = Cart(request)
    return render(request, "store/cart.html", {"cart": cart})


def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, "Your basket is empty. Add some products first.")
        return redirect("shop")

    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        phone = request.POST.get("phone", "").strip()
        address = request.POST.get("address", "").strip()
        notes = request.POST.get("notes", "").strip()

        if full_name and phone and address:
            order = Order.objects.create(
                full_name=full_name, phone=phone, address=address,
                notes=notes, total=cart.get_total(),
            )
            for item in cart:
                OrderItem.objects.create(
                    order=order, product=item["product"],
                    product_name=item["product"].name,
                    price=item["product"].price, quantity=item["quantity"],
                )
            cart.clear()
            return redirect("order_success", order_id=order.id)
        messages.error(request, "Please fill in your name, phone and address.")

    return render(request, "store/checkout.html", {"cart": cart})


def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "store/order_success.html", {"order": order})
