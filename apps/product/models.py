from django.db import models
from utils.django_models.field_choices import create_choices_tuple, code_to_name


# product_types = ['physical_product'
#                  'physical_book'
#                  'new_membership_subscription'
#                  'upgrade_membership_subscription'
#                  'sports_course_purchase']

# packing_slip_customization_choices = [
#     'generate_royalties_sheet',
#     'add_first_aid_video'
# ]

# product_pipeline_task_choices = [
#     'create_packing_slip',
#     'create_seller_commission_payment',
#     'create_royalties_payment',
#     'send_email_for_new_membership_subscription',
#     'send_email_for_upgrade_membership_subscription',
# ]


class PackingSlipCustomization(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductPipelineTask(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=50)
    pipeline_tasks = models.ManyToManyField('product.ProductPipelineTask')
    packing_slip_customizations = models.ManyToManyField('product.PackingSlipCustomization', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey('product.ProductType', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    weight = models.FloatField()
    price = models.FloatField()
    seller_commission_tax = models.FloatField()

    def __str__(self):
        return self.name