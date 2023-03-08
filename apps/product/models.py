from django.db import models
from django.utils import timezone
from utils.django_models.field_choices import create_choices_tuple, code_to_name


class ProductType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    pipeline = models.ForeignKey('tasks_pipeline.Pipeline', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Product(models.Model):
    sku = models.CharField(max_length=30, unique=True, blank=True, editable=False)
    name = models.CharField(max_length=255, unique=True)
    product_type = models.ForeignKey('product.ProductType', on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)
    weight = models.FloatField()
    price = models.FloatField()
    seller_commission_tax = models.FloatField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # creating SKU code
        if not self.sku:
            sku_prefix = '-'.join([initials.upper()[:3] for initials in self.product_type.name.split(' ')[:2]])
            sku_id = timezone.now().strftime('%y%m%d-%H%M%S-%f')[:17]
            self.sku = f'{sku_prefix}-{sku_id}'
        super().save(*args, **kwargs)

