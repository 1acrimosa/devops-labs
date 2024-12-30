from common.environ import env

# celery settings
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND", default="redis://redis:6379/1")
CELERY_BROKER_URL = env("CELERY_BROKER_URL", default="redis://redis:6379/2")

CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

CELERY_TASK_DEFAULT_QUEUE = "default"

CELERY_TASK_CREATE_MISSING_QUEUES = True
CELERY_TASK_IGNORE_RESULT = False

CELERY_TASK_ROUTES = {
    "*": {"queue": "default"},
}
