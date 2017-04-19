from django.contrib import admin

from django.apps import apps

from django.contrib.admin.sites import AlreadyRegistered

my_models = apps.get_app_config('groceries').get_models()
for model in my_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
