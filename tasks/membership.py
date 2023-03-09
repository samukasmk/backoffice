from core.celery import app


@app.task
def subscription(order_model_pk, task_function_args):
    print('create_membership_subscription:', order_model_pk, task_function_args)
    ...
