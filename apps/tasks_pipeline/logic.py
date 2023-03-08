import tasks as tasks_module


def get_pipeline_tasks(order_model):
    # task_function_names = order_model.ordered_products.all().values_list(
    #     'product__product_type__pipeline_tasks__code', flat=True).distinct()
    # return list(task_function_names)
    return []


def pipeline_runner(order_model):
    for task_function_name in get_pipeline_tasks(order_model):
        task_function = getattr(tasks_module, task_function_name)
        try:
            task_function(order_model.pk)
        except Exception as exc:
            print(exc)
