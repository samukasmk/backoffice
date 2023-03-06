from admin_site import admin
from apps.sales.models import Seller, Order


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
