from admin_site import admin
from apps.product.models import Product, ProductType


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'pipeline')
    search_fields = ('name',)
    autocomplete_fields = ('pipeline',)
    ordering = ('id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_type', 'sku', 'name', 'weight', 'price', 'seller_commission_tax')
    autocomplete_fields = ('product_type',)
    search_fields = ('name',)
    ordering = ('product_type', 'name',)
    list_filter = ('product_type',)