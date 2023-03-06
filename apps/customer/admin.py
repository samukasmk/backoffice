from admin_site import admin
from apps.customer.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
