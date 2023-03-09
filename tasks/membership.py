from celery import shared_task


@shared_task
def subscription(order_model_pk, task_function_args):
    print('create_membership_subscription:', order_model_pk, task_function_args)
    ...
