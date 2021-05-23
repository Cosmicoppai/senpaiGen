from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from post.models import Post
from users.models import User


def get_deleted_user_instance():
    return User.objects.get_or_create(nickname=_('Anon'))[0]  # Anon is the nickname/short-name for Anonomyous


class Like(models.Model):
    liked_user = models.ForeignKey(User, null=True, on_delete=models.SET(get_deleted_user_instance))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    like = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(1),
    ])
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Like')
        verbose_name_plural = _('Likes')

    def __str__(self):
        try:
            return "{} - {}".format(self.post.title, self.liked_user.nickname)
        except AttributeError:
            return "{} - {}".format(self.post.title, 'None')