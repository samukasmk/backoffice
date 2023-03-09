from core.celery import app


@app.task
def create_payment(order_model_pk, task_function_args):
    print('create_seller_commission_payment:', order_model_pk, task_function_args)
    ...
