from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.django_models.field_choices import create_choices_tuple
from logic.pipeline.runner import pipeline_runner
from logic.packing_slip.calcs import calculate_total_price, calculate_total_weigth, calculate_total_seller_commission

order_status = ['new', 'printed', 'picked', 'delivered']


class Seller(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class OrderedProduct(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey('sales.Order', on_delete=models.CASCADE, related_name='ordered_products')

    def total_price(self):
        return calculate_total_price(self.product.price, self.quantity)

    def total_weight(self):
        return calculate_total_weigth(self.product.weight, self.quantity)

    def total_seller_commission(self):
        return calculate_total_seller_commission(self.total_price(), self.product.seller_commission_tax)

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

    def order_total_price(self):
        return sum([ordered_product.total_price() for ordered_product in self.ordered_products.all()])

    def order_total_weight(self):
        return sum([ordered_product.total_weight() for ordered_product in self.ordered_products.all()])

    def order_total_seller_commission(self):
        return sum([ordered_product.total_seller_commission() for ordered_product in self.ordered_products.all()])


@receiver(post_save, sender=Order, dispatch_uid="trigger_to_run_pipeline")
def trigger_to_run_pipeline(sender, instance, created, **kwargs):
    if created:
        pipeline_runner(instance)
