from django.db import models
from django.utils import timezone
from core.utils.django_models.field_choices import create_choices_tuple

order_status = ['new', 'printed', 'picked', 'delivered']


class Seller(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)


class OrderedProduct(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Order(models.Model):
    order_status = models.CharField(max_length=30, choices=create_choices_tuple(order_status))
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    seller = models.ForeignKey('sales.Seller', on_delete=models.CASCADE)

    ordered_products = models.ManyToManyField('sales.OrderedProduct')

    delivery_note = models.FileField(upload_to="delivery_notes/", editable=False, null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now, editable=False, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, editable=False, blank=True)
