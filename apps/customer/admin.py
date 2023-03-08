from django.conf import settings
from admin_site import admin
from apps.customer.models import Customer, Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_type', 'name', 'tax_id', 'location', 'created_date')
    search_fields = ('name',)
    list_filter = ('customer_type', 'name',)
    ordering = ('customer_type', 'name',)

    def created_date(self, obj):
        return obj.created_at.strftime(settings.DEFAULT_TIME_FORMAT)