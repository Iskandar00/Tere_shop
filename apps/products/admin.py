from django.contrib import admin

from apps.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'price', 'created_at', 'updated_at',)
    prepopulated_fields = {'slug': ['title'], 'brand_slug': ['brand']}
    readonly_fields = ('updated_at', 'created_at')
    list_display_links = list_display
    search_fields = ('title', 'brand', 'price',)
