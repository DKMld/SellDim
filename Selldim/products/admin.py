from django.contrib import admin

from Selldim.products.models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator', 'product_name', 'price', 'category')
    list_filter = ('id', 'creator', 'product_name', 'price', 'category')


admin.site.register(Products, ProductsAdmin)
