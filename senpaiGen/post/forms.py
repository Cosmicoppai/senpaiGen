from .models import Post
from django import forms


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','id':"title-name",'placeholder':"Title" }),
            'body': forms.Textarea(attrs={'class':'form-control','id':"body-text",'placeholder':"Body/Text", 'rows':5}),
            'image': forms.FileInput(attrs={'class':'form-control', 'id':"image", 'accept':'image/*', 'placeholder':"Image"}),
        }