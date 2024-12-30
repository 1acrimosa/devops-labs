import logging
import os

from celery import Celery, Task

from common.settings.conf.installed_apps import INSTALLED_APPS


class BaseTask(Task):
    abstract = True
    _tasks: set = set()

    def __new__(cls):
        if "base" not in cls.__name__.lower() and cls.__name__ not in cls._tasks:  # type: ignore
            cls._tasks.add(cls.__name__)
            return cls.app.register_task(super(BaseTask, cls).__new__(cls))

    def success(self, response):
        pass

    def failed(self, response):
        pass

    def run(self):
        pass


logger = logging.getLogger(__name__)

# set the default Django settings module for the 'celery' program.
# if not ("DJANGO_SETTINGS_MODULE" in os.environ):
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "common.settings.dev")

app = Celery("app")
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'common.settings.celery')
# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object("django.conf:settings", namespace="CELERY")
BaseTask.bind(app=app)
app.autodiscover_tasks(lambda: INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    logger.info("Request: {0!r}".format(self.request))
