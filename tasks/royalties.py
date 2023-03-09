from celery import shared_task
from utils.django_models.dynamic_import import get_model_class


@shared_task
def create_payment(order_model_pk, task_function_args):
    RoyaltiesPayment = get_model_class('financial.RoyaltiesPayment')
    RoyaltiesPayment.objects.update_or_create(order_id=order_model_pk,
                                              defaults={'status': 'new'})
