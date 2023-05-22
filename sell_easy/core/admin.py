from django.contrib import admin

# Register your models here.

from .models import Store, Category, Products, Rating

admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Rating)