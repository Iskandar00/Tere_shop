from django.contrib import admin

from apps.basket.models import Basket


@admin.register(Basket)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product',)
    list_display_links = list_display
    search_fields = ('user', 'product',)
