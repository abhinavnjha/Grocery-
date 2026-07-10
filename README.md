# FreshKart — Grocery Mart Website (Django)

A modern, responsive grocery store website. No login or typing-heavy forms required —
products are shown with big pictures/icons so anyone, educated or not, can shop by tapping.

## Features
- Home page with categories, featured products, new arrivals
- Shop page with search, category filter, sort by price/name
- Product detail page with quantity stepper
- Session-based shopping cart (works without an account)
- Simple checkout (Cash on Delivery) that creates a real Order in the database
- Django Admin to manage Categories, Products, and Orders
- Fully responsive (mobile, tablet, desktop)

## How to run

1. Install Python 3.10+ and create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```

2. Install Django:
   ```
   pip install django
   ```

3. Run migrations:
   ```
   python manage.py migrate
   ```

4. Load sample products (29 grocery items across 6 categories):
   ```
   python manage.py seed_store
   ```

5. Create an admin login:
   ```
   python manage.py createsuperuser
   ```

6. Start the server:
   ```
   python manage.py runserver
   ```

7. Open in browser:
   - Store: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Managing products
Log in to /admin/ to add real products — give each one a name, price, category, and
either upload a real photo or just type an emoji (like 🍅) as a quick placeholder icon.
You can also set an "old price" to automatically show a discount badge.

## Notes for going live
- Set `DEBUG = False` and a real `SECRET_KEY` + `ALLOWED_HOSTS` in groceryhub/settings.py
- Switch the database from SQLite to PostgreSQL for production
- Add a real payment gateway if you need online payment (currently Cash on Delivery)
