from core.celery import app
from utils.django_models.dynamic_import import get_model_class
import tasks as tasks_module


@app.task
def pipeline_runner(model_class_ref, instance_pk):
    model_class = get_model_class(model_class_ref)
    instance_model = model_class.objects.get(pk=instance_pk)
    pipeline_details = instance_model.get_pipeline_details()

    for task_function_path, task_function_args in pipeline_details.items():
        task_function = getattr(tasks_module, task_function_path)
        try:
            task_function.delay(instance_model.pk, task_function_args)
        except Exception as exc:
            print(exc)
