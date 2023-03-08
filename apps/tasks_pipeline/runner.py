import tasks as tasks_module


def pipeline_runner(instance_model):
    pipeline_tasks = instance_model.get_pipeline_tasks()
    for task_function_name in pipeline_tasks:
        task_function = getattr(tasks_module, task_function_name)
        try:
            task_function.delay(instance_model.pk)
        except Exception as exc:
            print(exc)
