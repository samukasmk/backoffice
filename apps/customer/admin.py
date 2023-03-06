from admin_site import admin
from apps.customer.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_type', 'name', 'tax_id', 'city', 'state', 'country', 'created_at')
