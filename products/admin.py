from django.contrib import admin
from .models import Product, Category, Brand, League, SavedProducts


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'brand',
        'league',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class LeagueAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class SavedProductsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(League, LeagueAdmin)
admin.site.register(SavedProducts, SavedProductsAdmin)
