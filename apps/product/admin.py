from admin_site import admin
from apps.product.models import PackingSlipCustomization, ProductPipelineTask, ProductType, Product


@admin.register(PackingSlipCustomization)
class PackingSlipCustomizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


@admin.register(ProductPipelineTask)
class ProductPipelineTaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'weight', 'price', 'seller_commission_tax')
