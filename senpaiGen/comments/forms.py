from .models import Comments
from django import forms
from django.utils.translation import gettext as _


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment', )