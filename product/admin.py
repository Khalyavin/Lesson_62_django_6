from django.contrib import admin

from product.models import Product, Version

# Password 123
admin.site.register(Product)
admin.site.register(Version)
