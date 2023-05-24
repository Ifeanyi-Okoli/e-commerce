from django.contrib import admin

# Register your models here.

from .models import Store, Category, Products, Rating

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'tagline')
    list_filter = ('name', )
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'store', 'category', 'price')
    list_filter = ('name', 'store')
    list_per_page = 10


admin.site.register(Store, StoreAdmin)
admin.site.register(Category)
admin.site.register(Products, ProductAdmin)
admin.site.register(Rating)