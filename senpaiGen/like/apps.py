from django.apps import AppConfig


class LikeConfig(AppConfig):
    name = 'like'

    def ready(self):
        import like.signals  # General code here is:- import app_name.signals
