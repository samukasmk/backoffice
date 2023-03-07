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
                    'total_price', 'total_weigth',
                    'packing_slip_file', 'created_at')

    search_fields = ['customer__name']
    autocomplete_fields = ('customer', 'seller')
    inlines = [OrderedProductInLine]

    def total_price(self, obj):
        all_prices = [p.product.price * p.quantity for p in obj.ordered_products.all()]
        added_price = sum(all_prices)
        return '{0:.2f}'.format(added_price)

    def total_weigth(self, obj):
        all_weights = [p.product.weight * p.quantity for p in obj.ordered_products.all()]
        add_weight = sum(all_weights)
        return '{0:.2f}'.format(add_weight)


