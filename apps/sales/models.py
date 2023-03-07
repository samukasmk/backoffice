from django.db import models
from django.utils import timezone
from utils.django_models.field_choices import create_choices_tuple

order_status = ['new', 'printed', 'picked', 'delivered']


class Seller(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class OrderedProduct(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey('sales.Order', on_delete=models.CASCADE, related_name='ordered_products')

    def __str__(self):
        return f'{self.product.name}: {self.quantity}'


class Order(models.Model):
    order_status = models.CharField(max_length=30, choices=create_choices_tuple(order_status), default='new')
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    seller = models.ForeignKey('sales.Seller', on_delete=models.CASCADE)

    packing_slip_file = models.FileField(upload_to="packing_slips/", editable=False, null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now, editable=False, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, editable=False, blank=True)

    def __str__(self):
        return f'{self.pk} ({self.customer})'