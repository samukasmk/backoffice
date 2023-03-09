from core.celery import app


@app.task
def send_email_create_membership_subscription(order_model_pk, task_function_args):
    print('send_email_create_membership_subscription:', order_model_pk, task_function_args)
    ...


@app.task
def send_email_upgrade_membership_subscription(order_model_pk, task_function_args):
    print('send_email_upgrade_membership_subscription:', order_model_pk, task_function_args)
    ...
