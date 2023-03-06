from django.db import models
from utils.django_models.field_choices import create_choices_tuple

payment_status = ['new', 'approved', 'payed']


class SellerCommissionPayment(models.Model):
    order = models.ForeignKey('sales.Order', on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=create_choices_tuple(payment_status))

    def __str__(self):
        return f'Commission for seller: {self.order.seller.name}'

class RoyaltiesPayment(models.Model):
    order = models.ForeignKey('sales.Order', on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=create_choices_tuple(payment_status))
    def __str__(self):
        return f'Royalties for order: {self.order}'