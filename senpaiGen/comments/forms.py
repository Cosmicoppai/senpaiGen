from .models import Comments
from django import forms
from django.utils.translation import gettext as _


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)

        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control', 'id':'new-comment', 'placeholder':'Add a Comment', 'rows':5})
        }

        form_class = {
            'comment':'',
        }

        error_messages = {
            'comment':{
                'max_length': _('Comment should be less than 1000 Characters')
            }
        }