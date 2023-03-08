from core.celery import app


@app.task
def membership_subscription(order_model_pk):
    print('create_membership_subscription:', order_model_pk)
    ...
