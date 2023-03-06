from admin_site import admin
from apps.financial.models import SellerCommissionPayment, RoyaltiesPayment


@admin.register(SellerCommissionPayment)
class SellerCommissionPaymentAdmin(admin.ModelAdmin):
    pass


@admin.register(RoyaltiesPayment)
class RoyaltiesPaymentAdmin(admin.ModelAdmin):
    pass
