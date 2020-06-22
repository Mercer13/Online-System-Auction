from django.contrib import admin
from productpage.models import Product, Category
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)