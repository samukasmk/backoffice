from celery import shared_task


@shared_task
def send_email(order_model_pk, task_function_args):
    print('send_email:', order_model_pk, task_function_args)
    ...
