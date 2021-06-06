from django.db import models
from users.models import User
from post.models import Post
from django.utils.translation import gettext_lazy as _


def get_deleted_user_instance():
    return User.objects.get_or_create(nickname=_('Anon'))[0]  # Anon is the nickname/short-name for Anonomyous


class Comments(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET(get_deleted_user_instance))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=1000, blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        try:
            return "{} - {}".format(self.comment, self.author.nickname)
        except AttributeError:
            return "{} - {}".format(self.comment, 'None')