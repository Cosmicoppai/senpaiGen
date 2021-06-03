from .models import Post
from django import forms
from django.utils.translation import gettext as _


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': "title-name", 'placeholder': _("Title")}),
            'body': forms.Textarea(
                attrs={'class': 'form-control', 'id': "body-text", 'placeholder': _("Body"), 'rows': 5}),
            'image': forms.FileInput(
                attrs={'class': 'form-control', 'id': "image", 'accept': 'image/*', 'placeholder': _("Image")}),
        }

        labels = {
            'title': '',
            'body': '',
            'image': '',
        }

        help_texts = {
            'title': _('Enter the Title of the Post'),
            'body': _('Describe your Question Properly'),
            'image': _('Only "jpg, png, jpeg" formats are allowed')
        }

        error_messages = {
            'title': {
                'max_length': _('Title should be of length less than or equal to 100 characters'),
            },
            'body': {
                'max_length': _('Body should be of length less than or equal to 10000 characters'),
            },
            'image':{
                'validation': _('Enter a Valid Image Format (jpg, png, jpeg)'),
            }
        }
