from celery import shared_task


@shared_task
def create_payment(order_model_pk, task_function_args):
    print('create_royalties_payment:', order_model_pk, task_function_args)
    ...
