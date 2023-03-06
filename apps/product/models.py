from django.db import models
from utils.django_models.field_choices import create_choices_tuple

# product_types = ['physical_product'
#                  'physical_book'
#                  'new_membership_subscription'
#                  'upgrade_membership_subscription'
#                  'sports_course_purchase']

packing_slip_customization_choices = [
    'generate_royalties_sheet',
    'add_first_aid_video'
]

product_pipeline_task_choices = [
    'create_delivery_note',
    'create_seller_commission_payment',
    'create_royalties_payment',
    'send_email_for_new_membership_subscription',
    'send_email_for_upgrade_membership_subscription',
]


class PackingSlipCustomization(models.Model):
    customization = models.CharField(max_length=100, choices=create_choices_tuple(packing_slip_customization_choices))


class ProductPipelineTask(models.Model):
    task = models.CharField(max_length=100, choices=create_choices_tuple(product_pipeline_task_choices))


class ProductType(models.Model):
    name = models.CharField(max_length=50)
    packing_slip_customizations = models.ManyToManyField('product.PackingSlipCustomization')
    pipeline_tasks = models.ManyToManyField('product.ProductPipelineTask')


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    weight = models.FloatField()
    seller_commission_tax = models.FloatField()
    product_type = models.ForeignKey('product.ProductType', on_delete=models.CASCADE)
