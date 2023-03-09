from core.celery import app


@app.task
def create_royalties_payment(order_model_pk, task_function_args):
    print('create_royalties_payment:', order_model_pk, task_function_args)
    ...
