from rest_framework import serializers
from .models import Category, Product, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    """Serves as the 'Menu' API — lists items with price and stock."""
    class Meta:
        model = Product
        fields = [
            'id', 'category', 'name', 'slug', 'description',
            'price', 'old_price', 'unit', 'stock', 'is_featured', 'created_at',
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'price', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    """Serves as the 'Booking' API — customer places an order for a slot/date."""
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'full_name', 'phone', 'address', 'notes',
            'status', 'total', 'created_at', 'items',
        ]
