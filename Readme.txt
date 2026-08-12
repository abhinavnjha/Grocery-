FreshKart / GroceryHub API - Endpoints to Test

Product API (acts as the "Menu"):
/api/products/
/api/products/<id>/

Category API:
/api/categories/
/api/categories/<id>/

Order API (acts as "Booking" - place and track orders):
/api/orders/
/api/orders/<id>/

Authentication (Djoser):
/auth/users/                (register a new user)
/auth/token/login/          (obtain auth token)
/auth/token/logout/         (destroy auth token)

Admin panel:
/admin/

Storefront (HTML pages):
/                            (home page)
/shop/                       (shop with search/filter/sort)
/cart/                       (shopping cart)
/checkout/                   (checkout - creates an Order)

Setup instructions:
1. pip install -r requirements.txt
2. Configure MySQL database credentials in groceryhub/settings.py
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py seed_store   (optional - loads sample products)
6. python manage.py createsuperuser
7. python manage.py runserver
