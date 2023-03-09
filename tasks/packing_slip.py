from celery import shared_task


@shared_task
def create_pdf_file(order_model_pk, task_function_args):
    print('create_packing_slip:', order_model_pk, task_function_args)
    ...
