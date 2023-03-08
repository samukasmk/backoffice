from core.celery import app


@app.task
def create_packing_slip(order_model_pk):
    print('create_packing_slip:', order_model_pk)
    ...
