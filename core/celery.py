import os
from celery import Celery
from core.tasks import ALLOWED_TASKS

# Set default configuration module name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# declare celery app
app = Celery('core')

# load configs from django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# discovery tasks from django apps
app.autodiscover_tasks()

# disable results
app.conf.result_expires = 0
app.conf.task_ignore_result = True
app.conf.task_store_errors_even_if_ignored = False

# define queue routes for bulting tasks in django apps
app.conf.task_routes = {
    'apps.tasks_pipeline.tasks.pipeline_runner': {'queue': 'pipeline_runner'}
}

# define queue routes for pipeline tasks at external modules
for task_module in ALLOWED_TASKS:
    package_path = f'tasks.{task_module}'
    app.conf.task_routes[package_path] = {'queue': package_path}
