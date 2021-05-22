from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.conf import settings
from .models import UserData
from django.core.exceptions import ObjectDoesNotExist


User = get_user_model()


def post_save_user_model_received(sender, instance, created, *args, **kwargs):
    if created:
        try:
            UserData.objects.create(user=instance)
        except ObjectDoesNotExist:
            pass


post_save.connect(post_save_user_model_received, sender=settings.AUTH_USER_MODEL)


def pre_save_delete_files_on_change(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_profile_pic = UserData.objects.get(pk=instance.pk).profile_pic
        except User.DoesNotExist:
            return
        new_profile_pic = instance.profile_pic
        if old_profile_pic and old_profile_pic.url != new_profile_pic.url:
            old_profile_pic.delete(save=False)


pre_save.connect(pre_save_delete_files_on_change, sender=UserData)
