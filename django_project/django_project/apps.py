from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "django_project"

    def ready(self):
        import_module("django_project.receivers")


class JobsConfig(BaseAppConfig):
    name = 'jobs'
