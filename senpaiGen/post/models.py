from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User
import PIL.Image as Image


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author'))
    title = models.CharField(verbose_name=_('Title'), max_length=50, blank=False, null=False)
    body = models.TextField(verbose_name=_('Body'), max_length=1000, null=False, blank=False)
    image = models.ImageField(verbose_name=_('Image'), blank=True, null=True, upload_to='post')
    date_added = models.DateTimeField(verbose_name=_('Asked on'), auto_now_add=True)
    total_no_of_likes = models.PositiveIntegerField(verbose_name=_('Total no of likes'), blank=True, default=0)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _("Post's")

    def __str__(self):
        return "{} - {} -    {}".format(self.author, self.title, self.date_added)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 1200 and img.width > 675:
            output_size = (1200, 675)
            img.thumbnail(output_size)
            img.save(self.image.path)
