from celery import shared_task
from utils.django_models.dynamic_import import get_model_class

@shared_task
def subscription(order_model_pk, task_function_args):
    Order = get_model_class('sales.Order')
    instance_model = Order.objects.get(pk=order_model_pk)
