from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    name = 'marketplace_api'


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'marketplace_api'


class CategoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'marketplace_api'
