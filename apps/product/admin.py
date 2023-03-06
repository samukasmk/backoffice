from admin_site import admin
from apps.product.models import PackingSlipCustomization, ProductPipelineTask, ProductType, Product


@admin.register(PackingSlipCustomization)
class PackingSlipCustomizationAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductPipelineTask)
class ProductPipelineTaskAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
