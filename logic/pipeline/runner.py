from logic.pipeline import tasks

def get_pipeline_tasks(order_model):
    pipeline_tasks = {}
    for ordered_product in order_model.ordered_products.all():
        tasks = ordered_product.product.product_type.pipeline_tasks.all().values_list('code', flat=True)
        for task_code in tasks:
            pipeline_tasks[task_code] = pipeline_tasks.get(task_code, [])
            pipeline_tasks[task_code].append(ordered_product)
    return pipeline_tasks


def pipeline_runner(order_model):
    for task_function_name, task_args in get_pipeline_tasks(order_model).items():
        task = getattr(tasks, task_function_name)
        try:
            task(task_args)
        except Exception as exc:
            print(exc)
