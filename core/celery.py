import os
from celery import Celery
from django.conf import settings

# Set default configuration module name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('backoffice')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.result_expires = 0
app.conf.task_ignore_result = True
app.conf.task_store_errors_even_if_ignored = False

# task route and queue definitions
app.conf.task_routes = {
    'tasks.packing_slip.create_packing_slip': {'queue': 'create_packing_slip'},
    'tasks.seller_commission.create_seller_commission_payment': {'queue': 'create_seller_commission_payment'},
    'tasks.royalties.create_royalties_payment': {'queue': 'create_royalties_payment'},
    'tasks.membership.membership_subscription': {'queue': 'membership_subscription'},
    'tasks.send_email.send_email': {'queue': 'send_email'},
}