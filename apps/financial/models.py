from django.db import models
from utils.django_models.field_choices import create_choices_tuple

payment_status = ['new', 'approved', 'payed']


class FinancialAnalyst(models.Model):
    name = models.CharField(max_length=255)


class SellerCommissionPayment(models.Model):
    order = models.ForeignKey('sales.Order', on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=create_choices_tuple(payment_status))


class RoyaltiesPayment(models.Model):
    order = models.ForeignKey('sales.Order', on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=create_choices_tuple(payment_status))
