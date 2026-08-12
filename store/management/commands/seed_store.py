from django.core.management.base import BaseCommand
from store.models import Category, Product


CATEGORIES = [
    ("Fruits & Vegetables", "🍎", "fruits-vegetables"),
    ("Dairy & Bakery", "🥛", "dairy-bakery"),
    ("Staples", "🌾", "staples"),
    ("Snacks & Beverages", "🍪", "snacks-beverages"),
    ("Household", "🧴", "household"),
    ("Personal Care", "🧼", "personal-care"),
]

PRODUCTS = [
    ("fruits-vegetables", "Fresh Tomato", "🍅", 30, None, "kg"),
    ("fruits-vegetables", "Banana", "🍌", 40, 50, "dozen"),
    ("fruits-vegetables", "Broccoli", "🥦", 60, None, "kg"),
    ("fruits-vegetables", "Onion", "🧅", 28, 35, "kg"),
    ("fruits-vegetables", "Potato", "🥔", 25, None, "kg"),
    ("fruits-vegetables", "Apple (Shimla)", "🍎", 150, 180, "kg"),
    ("dairy-bakery", "Toned Milk", "🥛", 28, None, "l"),
    ("dairy-bakery", "Brown Bread", "🍞", 45, None, "pack"),
    ("dairy-bakery", "Paneer", "🧀", 90, 100, "g"),
    ("dairy-bakery", "Farm Eggs", "🥚", 70, None, "dozen"),
    ("dairy-bakery", "Butter", "🧈", 55, None, "g"),
    ("staples", "Basmati Rice", "🍚", 120, 140, "kg"),
    ("staples", "Wheat Atta", "🌾", 65, None, "kg"),
    ("staples", "Toor Dal", "🫘", 140, None, "kg"),
    ("staples", "Sunflower Oil", "🛢️", 180, 200, "l"),
    ("staples", "Sugar", "🧂", 48, None, "kg"),
    ("snacks-beverages", "Potato Chips", "🍟", 20, None, "pack"),
    ("snacks-beverages", "Cola Soft Drink", "🥤", 40, None, "l"),
    ("snacks-beverages", "Biscuits", "🍪", 30, 35, "pack"),
    ("snacks-beverages", "Orange Juice", "🧃", 99, None, "l"),
    ("snacks-beverages", "Tea Powder", "🍵", 150, None, "pack"),
    ("household", "Dish Wash Liquid", "🧴", 85, 95, "l"),
    ("household", "Laundry Detergent", "🧺", 210, None, "kg"),
    ("household", "Trash Bags", "🗑️", 60, None, "pack"),
    ("household", "Floor Cleaner", "🧹", 110, None, "l"),
    ("personal-care", "Bath Soap", "🧼", 35, 40, "pc"),
    ("personal-care", "Shampoo", "🧴", 150, 170, "pack"),
    ("personal-care", "Toothpaste", "🪥", 55, None, "pc"),
    ("personal-care", "Hand Sanitizer", "🧴", 65, None, "l"),
]


class Command(BaseCommand):
    help = "Seed the database with sample grocery categories and products"

    def handle(self, *args, **options):
        cat_objs = {}
        for name, icon, slug in CATEGORIES:
            cat, _ = Category.objects.update_or_create(
                slug=slug, defaults={"name": name, "icon": icon}
            )
            cat_objs[slug] = cat
        self.stdout.write(self.style.SUCCESS(f"Categories ready: {len(cat_objs)}"))

        created = 0
        for i, (cat_slug, name, emoji, price, old_price, unit) in enumerate(PRODUCTS):
            slug = name.lower().replace(" ", "-").replace("(", "").replace(")", "")
            _, was_created = Product.objects.update_or_create(
                slug=slug,
                defaults={
                    "category": cat_objs[cat_slug],
                    "name": name,
                    "emoji": emoji,
                    "price": price,
                    "old_price": old_price,
                    "unit": unit,
                    "stock": 50,
                    "is_featured": i % 5 == 0,
                },
            )
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Products ready: {len(PRODUCTS)} (new: {created})"))
