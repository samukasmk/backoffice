from admin_site import admin
from apps.product.models import PackingSlipCustomization, ProductPipelineTask, ProductType, Product


@admin.register(PackingSlipCustomization)
class PackingSlipCustomizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name',)

@admin.register(ProductPipelineTask)
class ProductPipelineTaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name',)


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    autocomplete_fields = ('pipeline_tasks', 'packing_slip_customizations')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'weight', 'price', 'seller_commission_tax')
    autocomplete_fields = ('product_type',)
    search_fields = ('name',)