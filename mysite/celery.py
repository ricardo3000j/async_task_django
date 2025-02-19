import os
from celery import Celery


# Setting the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
app = Celery("mysite")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.update(
    {"imports": ("polls.tasks"), "task_routes": ("polls.task_router.SurveyRouter")}
)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
