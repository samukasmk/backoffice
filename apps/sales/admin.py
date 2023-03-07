from admin_site import admin
from apps.sales.models import Seller, Order, OrderedProduct


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


@admin.register(OrderedProduct)
class OrderedProductAdmin(admin.ModelAdmin):
    pass


class OrderedProductInLine(admin.TabularInline):
    model = OrderedProduct
    extra = 1
    autocomplete_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'seller', 'order_status',
                    'total_price', 'total_weight', 'total_seller_commission',
                    'packing_slip_file', 'created_at')

    search_fields = ['customer__name']
    autocomplete_fields = ('customer', 'seller')
    inlines = [OrderedProductInLine]

    def total_price(self, obj):
        return '{0:.2f}'.format(obj.order_total_price())

    def total_weight(self, obj):
        return '{0:.2f}'.format(obj.order_total_weight())

    def total_seller_commission(self, obj):
        return '{0:.2f}'.format(obj.order_total_seller_commission())
