from django.contrib import admin

from Selldim.common.models import ProductLikes


class ProductLikesAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    list_filter = ('user', 'product')


admin.site.register(ProductLikes, ProductLikesAdmin)


