from core.celery import app


@app.task
def create_packing_slip(order_model_pk, task_function_args):
    print('create_packing_slip:', order_model_pk, task_function_args)
    ...
