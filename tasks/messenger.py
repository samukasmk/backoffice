from core.celery import app


@app.task
def send_email(order_model_pk, task_function_args):
    print('send_email:', order_model_pk, task_function_args)
    ...