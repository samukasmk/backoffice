from core.celery import app


@app.task
def create_seller_commission_payment(order_model_pk):
    print('create_seller_commission_payment:', order_model_pk)
    ...
