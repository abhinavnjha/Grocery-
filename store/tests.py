from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Category, Product, Order


class ProductModelTest(TestCase):
    def test_create_product(self):
        category = Category.objects.create(name="Fruits", slug="fruits")
        product = Product.objects.create(
            category=category, name="Apple", slug="apple", price=120
        )
        self.assertEqual(str(product), "Apple")
        self.assertTrue(product.in_stock)


class OrderModelTest(TestCase):
    def test_create_order(self):
        order = Order.objects.create(
            full_name="Jane Doe", phone="9999999999",
            address="123 Street", total=250,
        )
        self.assertEqual(order.status, "pending")


class ProductAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name="Dairy", slug="dairy")
        self.product = Product.objects.create(
            category=self.category, name="Milk", slug="milk", price=60
        )

    def test_list_products_unauthenticated(self):
        # Read access is allowed without auth (IsAuthenticatedOrReadOnly)
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OrderAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass123")

    def test_orders_require_authentication(self):
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_orders_accessible_when_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
