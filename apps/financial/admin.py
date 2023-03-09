from django.conf import settings
from admin_site import admin
from apps.financial.models import SellerCommissionPayment, RoyaltiesPayment


@admin.register(SellerCommissionPayment)
class SellerCommissionPaymentAdmin(admin.ModelAdmin):
    list_display = ('order_code', 'payment_status', 'seller', 'customer', 'order_created_at', 'total_seller_commission')
    ordering = ('id',)
    list_filter = ('status', 'order__seller__name',)
    search_fields = ('order__code',)

    def order_code(self, obj):
        return obj.order.code

    def payment_status(self, obj):
        return obj.status

    def customer(self, obj):
        return obj.order.customer.name

    def seller(self, obj):
        return obj.order.seller.name

    def order_created_at(self, obj):
        return obj.order.created_at.strftime(settings.DEFAULT_TIME_FORMAT)

    def total_seller_commission(self, obj):
        return '${0:.2f}'.format(obj.order.order_total_seller_commission())

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(RoyaltiesPayment)
class RoyaltiesPaymentAdmin(admin.ModelAdmin):
    list_display = ('order_code', 'payment_status', 'customer', 'order_created_at', 'royalties_gross_price')
    ordering = ('id',)
    list_filter = ('status', 'order__seller__name',)
    search_fields = ('order__code',)

    def order_code(self, obj):
        return obj.order.code

    def payment_status(self, obj):
        return obj.status

    def customer(self, obj):
        return obj.order.customer.name

    def order_created_at(self, obj):
        return obj.order.created_at.strftime(settings.DEFAULT_TIME_FORMAT)

    def royalties_gross_price(self, obj):
        return '${0:.2f}'.format(obj.royalties_gross_price())

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
