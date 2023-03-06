from admin_site import admin
from apps.sales.models import Seller, Order, OrderedProduct


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderedProduct)
class OrderedProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'seller', 'order_status',
                    'total_price', 'total_weigth',
                    'packing_slip_file', 'created_at')

    def total_price(self, obj):
        return sum([p.product.price * p.quantity for p in obj.ordered_products.all()])

    def total_weigth(self, obj):
        return sum([p.product.weight * p.quantity for p in obj.ordered_products.all()])
