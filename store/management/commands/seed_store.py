from django.core.management.base import BaseCommand
from store.models import Category, Product

CATEGORIES = [
    ("Fruits & Vegetables", "🍎", "fruits-vegetables",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg/640px-Good_Food_Display_-_NCI_Visuals_Online.jpg"),
    ("Dairy & Bakery", "🥛", "dairy-bakery",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Oberhasli_Dairy_Goat.jpg/640px-Oberhasli_Dairy_Goat.jpg"),
    ("Staples", "🌾", "staples",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Wheat_close-up.JPG/640px-Wheat_close-up.JPG"),
    ("Snacks & Beverages", "🍪", "snacks-beverages",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat_03.jpg/481px-Cat_03.jpg"),
    ("Household", "🧴", "household",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Cleaning_Supplies.jpg/640px-Cleaning_Supplies.jpg"),
    ("Personal Care", "🧼", "personal-care",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Soaps.jpg/640px-Soaps.jpg"),
]

# (cat_slug, name, slug, price, old_price, unit, image_url, description, featured)
PRODUCTS = [
  # --- Fruits & Vegetables ---
  ("fruits-vegetables","Fresh Tomato","fresh-tomato",30,None,"kg",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Tomato_je.jpg/640px-Tomato_je.jpg",
   "Sun-ripened juicy tomatoes, perfect for curries, salads and chutneys.",True),

  ("fruits-vegetables","Banana","banana",40,50,"dozen",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Banana-Fruits.jpg/640px-Banana-Fruits.jpg",
   "Sweet, ripe Cavendish bananas. Great for breakfast or a quick snack.",False),

  ("fruits-vegetables","Broccoli","broccoli",60,None,"kg",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Broccoli_and_cross_section_edit.jpg/640px-Broccoli_and_cross_section_edit.jpg",
   "Fresh green broccoli — packed with vitamins C and K.",False),

  ("fruits-vegetables","Onion","onion",28,35,"kg",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Onions.jpg/640px-Onions.jpg",
   "Farm-fresh red onions. A must-have base for every Indian dish.",True),

  ("fruits-vegetables","Potato","potato",25,None,"kg",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Patates.jpg/640px-Patates.jpg",
   "Versatile, starchy potatoes — for aloo sabzi, fries, soups and more.",False),

  ("fruits-vegetables","Apple (Shimla)","apple-shimla",150,180,"kg",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Apple.jpg/640px-Red_Apple.jpg",
   "Crunchy Shimla apples. Sweet, fresh and great for kids.",True),

  ("fruits-vegetables","Carrot","carrot",45,None,"kg",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Vegetable-Carrot-Bundle-wStalks.jpg/640px-Vegetable-Carrot-Bundle-wStalks.jpg",
   "Bright orange carrots — perfect for halwa, salads and juices.",False),

  ("fruits-vegetables","Spinach","spinach",30,None,"pack",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Baby-spinach.jpg/640px-Baby-spinach.jpg",
   "Fresh, tender spinach leaves. Great for palak paneer and smoothies.",False),

  # --- Dairy & Bakery ---
  ("dairy-bakery","Toned Milk","toned-milk",28,None,"l",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Milk_glass.jpg/640px-Milk_glass.jpg",
   "Fresh toned milk. Delivered daily, full of calcium and protein.",True),

  ("dairy-bakery","Brown Bread","brown-bread",45,None,"pack",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Half_a_dozen_bread_rolls.jpg/640px-Half_a_dozen_bread_rolls.jpg",
   "Soft whole-wheat brown bread, baked fresh every morning.",False),

  ("dairy-bakery","Paneer","paneer",90,100,"g",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Paneer_%28fromage_cottage_indien%29.jpg/640px-Paneer_%28fromage_cottage_indien%29.jpg",
   "Fresh, soft paneer made from full-fat milk. Ideal for paneer butter masala.",True),

  ("dairy-bakery","Farm Eggs","farm-eggs",70,None,"dozen",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Chicken_eggs_2009c.jpg/640px-Chicken_eggs_2009c.jpg",
   "Free-range farm-fresh eggs. Rich yolk, high protein.",False),

  ("dairy-bakery","Butter","butter",55,None,"g",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Budae-jjigae_%28army_stew%29_%286278647548%29.jpg/640px-Budae-jjigae_%28army_stew%29_%286278647548%29.jpg",
   "Creamy salted butter — perfect on toast, parathas and dal.",False),

  ("dairy-bakery","Curd / Dahi","curd-dahi",30,None,"g",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Plain-yogurt.jpg/640px-Plain-yogurt.jpg",
   "Fresh, thick homestyle curd. Great with meals or as lassi.",True),

  # --- Staples ---
  ("staples","Basmati Rice","basmati-rice",120,140,"kg",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Rice_p1160004.jpg/640px-Rice_p1160004.jpg",
   "Long-grain fragrant basmati rice. Cooks fluffy and separate.",True),

  ("staples","Wheat Atta","wheat-atta",65,None,"kg",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Wheat_milling_-_freshly_ground_atta.jpg/640px-Wheat_milling_-_freshly_ground_atta.jpg",
   "Stone-ground whole wheat atta for soft, healthy rotis.",False),

  ("staples","Toor Dal","toor-dal",140,None,"kg",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Dal_makhani.jpg/640px-Dal_makhani.jpg",
   "Premium yellow toor dal — the base of every good Indian dal tadka.",False),

  ("staples","Sunflower Oil","sunflower-oil",180,200,"l",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Sunflower_Seeds_Kaldari.jpg/640px-Sunflower_Seeds_Kaldari.jpg",
   "Light refined sunflower oil — low cholesterol, great for cooking.",False),

  ("staples","Sugar","sugar",48,None,"kg",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Cane_sugar_from_Guyana.jpg/640px-Cane_sugar_from_Guyana.jpg",
   "Fine white crystal sugar for tea, desserts and cooking.",True),

  ("staples","Chana Dal","chana-dal",110,None,"kg",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Channa_daal.JPG/640px-Channa_daal.JPG",
   "High-protein split chickpea dal — great for soups and halwa.",False),

  # --- Snacks & Beverages ---
  ("snacks-beverages","Potato Chips","potato-chips",20,None,"pack",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Potato-Chips.jpg/640px-Potato-Chips.jpg",
   "Crispy, salted potato chips — perfect evening snack.",False),

  ("snacks-beverages","Orange Juice","orange-juice",99,None,"l",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Oranges_and_orange_juice.jpg/640px-Oranges_and_orange_juice.jpg",
   "100% real squeezed orange juice. No added sugar.",True),

  ("snacks-beverages","Biscuits","biscuits",30,35,"pack",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Biscuits-Pile.jpg/640px-Biscuits-Pile.jpg",
   "Classic crunchy biscuits — great with chai.",False),

  ("snacks-beverages","Tea Powder","tea-powder",150,None,"pack",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Graine_de_th%C3%A9.JPG/640px-Graine_de_th%C3%A9.JPG",
   "Strong Assam CTC tea powder. Brews a rich, aromatic cup.",True),

  ("snacks-beverages","Instant Coffee","instant-coffee",220,250,"pack",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/A_small_cup_of_coffee.JPG/640px-A_small_cup_of_coffee.JPG",
   "Rich, smooth instant coffee. Ready in seconds.",False),

  # --- Household ---
  ("household","Dish Wash Liquid","dish-wash-liquid",85,95,"l",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Washing_up_liquid.jpg/640px-Washing_up_liquid.jpg",
   "Powerful grease-cutting dish wash liquid. Gentle on hands.",False),

  ("household","Laundry Detergent","laundry-detergent",210,None,"kg",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Washing_machine_open_door.JPG/640px-Washing_machine_open_door.JPG",
   "Front-load friendly detergent powder — tough on stains, gentle on fabric.",True),

  ("household","Floor Cleaner","floor-cleaner",110,None,"l",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Cleaning-equipment.jpg/640px-Cleaning-equipment.jpg",
   "Disinfectant floor cleaner — kills 99.9% germs, leaves a fresh fragrance.",False),

  # --- Personal Care ---
  ("personal-care","Bath Soap","bath-soap",35,40,"pc",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Glycerin_soap.JPG/640px-Glycerin_soap.JPG",
   "Moisturising bath soap with natural fragrance. Gentle on all skin types.",True),

  ("personal-care","Shampoo","shampoo",150,170,"pack",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Shampoo_at_Hanoi_market.jpg/640px-Shampoo_at_Hanoi_market.jpg",
   "Nourishing shampoo with keratin. Reduces hair fall and adds shine.",False),

  ("personal-care","Toothpaste","toothpaste",55,None,"pc",
   "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Toothbrush_with_paste.jpg/640px-Toothbrush_with_paste.jpg",
   "Cavity protection toothpaste with fluoride and mint freshness.",False),
]


class Command(BaseCommand):
    help = "Seed the database with real grocery categories and products"

    def handle(self, *args, **options):
        cat_objs = {}
        for name, icon, slug, img_url in CATEGORIES:
            cat, _ = Category.objects.update_or_create(
                slug=slug, defaults={"name": name, "icon": icon, "image_url": img_url}
            )
            cat_objs[slug] = cat
        self.stdout.write(self.style.SUCCESS(f"Categories ready: {len(cat_objs)}"))

        created = 0
        for (cat_slug, name, slug, price, old_price, unit,
             image_url, description, featured) in PRODUCTS:
            _, was_created = Product.objects.update_or_create(
                slug=slug,
                defaults={
                    "category": cat_objs[cat_slug],
                    "name": name,
                    "image_url": image_url,
                    "emoji": "",
                    "price": price,
                    "old_price": old_price,
                    "unit": unit,
                    "description": description,
                    "stock": 80,
                    "is_featured": featured,
                },
            )
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Products ready: {len(PRODUCTS)} (new: {created})"))
