from celery import shared_task
from utils.django_models.dynamic_import import get_model_class


@shared_task
def create_payment(order_model_pk, task_function_args):
    SellerCommissionPayment = get_model_class('financial.SellerCommissionPayment')
    SellerCommissionPayment.objects.create(order_id=1, status='new')
