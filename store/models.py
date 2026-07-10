from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=10, default="🛒")
    slug = models.SlugField(unique=True)
    image_url = models.URLField(blank=True, help_text="Real photo URL for this category")

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    UNIT_CHOICES = [
        ("kg", "per kg"), ("g", "per 500g"), ("pc", "per piece"),
        ("l", "per litre"), ("pack", "per pack"), ("dozen", "per dozen"),
    ]

    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    image_url = models.URLField(blank=True, help_text="External photo URL (used if no image uploaded)")
    emoji = models.CharField(max_length=10, default="🛒")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    old_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default="pc")
    stock = models.PositiveIntegerField(default=100)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.slug])

    @property
    def photo(self):
        """Returns the best available image src — uploaded file, external URL, or None."""
        if self.image:
            return self.image.url
        if self.image_url:
            return self.image_url
        return None

    @property
    def in_stock(self):
        return self.stock > 0

    @property
    def discount_percent(self):
        if self.old_price and self.old_price > self.price:
            return round((self.old_price - self.price) / self.old_price * 100)
        return 0


class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"), ("confirmed", "Confirmed"), ("delivered", "Delivered"),
    ]
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    notes = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.full_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.product_name} x {self.quantity}"
