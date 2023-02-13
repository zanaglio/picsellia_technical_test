from celery import Celery

CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "redis://redis:6379/0"

celery = Celery("celery", backend=CELERY_BROKER_URL, broker=CELERY_RESULT_BACKEND, include=["tasks"])
celery.conf.task_routes = (
    [
        ("outline.objects.tasks.*", {"queue": "outline"}),
    ],
)

celery.conf.result_expires = 120
