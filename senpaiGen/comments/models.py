from django.db import models
from users.models import User
from post.models import Post
from django.utils.translation import gettext_lazy as _


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.ObjectDoesNotExist)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=500, blank=True, null=True, verbose_name=_('Comment'))
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return "{}- {}".format(self.comment, self.author.nickname)