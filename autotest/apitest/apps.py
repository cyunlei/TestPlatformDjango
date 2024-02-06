from django.apps import AppConfig


class ApitestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apitest'


class ApiStepConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apistep'


class ApisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apis'
