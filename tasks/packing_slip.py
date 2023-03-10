import os
import pdfkit
from django.template import loader
from celery import shared_task
from utils.django_models.dynamic_import import get_model_class
from apps.tasks_pipeline.logic import monitoring_pipeline_task


@shared_task
@monitoring_pipeline_task('packing_slip.create_pdf_file', 'sales.Order')
def create_pdf_file(model_instance_pk, task_arguments, *args, **kwargs):

    if os.path.exists("/tmp/out.pdf"):
        os.remove("/tmp/out.pdf")

    content_html = loader.render_to_string(template_name='packing_slip/packing_slip.html',
                                           context={'order': kwargs['model_instance']},
                                           request=None)
    pdfkit.from_string(content_html, '/tmp/out.pdf')