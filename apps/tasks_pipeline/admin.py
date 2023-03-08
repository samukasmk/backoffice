from django.conf import settings
from admin_site import admin
from apps.product.models import ProductType, Product

from apps.tasks_pipeline.models import Task, TaskArgument, Pipeline, PipelineTask, Monitoring

# Task admin
class TaskArgumentInLineAdmin(admin.TabularInline):
    model = TaskArgument
    extra = 1

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'path', 'arguments')
    search_fields = ('name', 'path')
    ordering = ('id',)
    inlines = [TaskArgumentInLineAdmin]

    def arguments(self, obj):
        return ', '.join(obj.get_arguments())

# Pipeline admin
class PipelineTaskInLineAdmin(admin.TabularInline):
    model = PipelineTask
    extra = 1

@admin.register(Pipeline)
class PipelineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'tasks')
    search_fields = ('name',)
    ordering = ('id',)

    inlines = [PipelineTaskInLineAdmin]


    def tasks(self, obj):
        names = obj.tasks.all().values_list('task__name', flat=True)
        ordered_names = [f'({index+1}) {name}' for index, name in enumerate(names)]
        return ' -> '.join(list(ordered_names))


@admin.register(Monitoring)
class MonitoringAdmin(admin.ModelAdmin):
    list_display = ('status', 'pipeline_name', 'task_name', 'task_path', 'task_arguments', 'created_at', 'updated_at')
    list_filter = ('status',)
    ordering = ('-id',)

    def pipeline_name(self, obj):
        return obj.pipeline_task_execution.pipeline.name

    def task_name(self, obj):
        return obj.pipeline_task_execution.task.name

    def task_path(self, obj):
        return obj.pipeline_task_execution.task.path

    def task_arguments(self, obj):
        return ', '.join(obj.pipeline_task_execution.task.get_arguments())

    def created_at(self, obj):
        return obj.pipeline_task_execution.created_at.strftime(settings.DEFAULT_TIME_FORMAT)

    def updated_at(self, obj):
        return obj.pipeline_task_execution.updated_at.strftime(settings.DEFAULT_TIME_FORMAT)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

