from celery import shared_task
from utils.django_models.dynamic_import import get_model_class
from tasks import registered_tasks


@shared_task
def pipeline_runner(model_class_ref, instance_pk):
    model_class = get_model_class(model_class_ref)
    instance_model = model_class.objects.get(pk=instance_pk)
    pipeline_details = instance_model.get_pipeline_details()

    for task_function_path, task_function_args in pipeline_details.items():
        try:
            task_function = registered_tasks.get(task_function_path)
            task_function.delay(instance_model.pk, task_function_args)
        except Exception as exc:
            print(exc)
