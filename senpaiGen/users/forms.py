from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
from .collegelist import College_list
from .models import UserData

User = get_user_model()


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('nickname', 'email',)

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password didn't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('nickname', 'email', 'password', 'admin', 'active')

    def clean_password(self):
        return self.initial["password"]


class LoginForm(forms.Form):
    nickname = forms.CharField(label='Nickname')
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        nickname = self.cleaned_data.get("nickname")
        password = self.cleaned_data.get("password")

        user_obj = User.objects.filter(nickname=nickname).first()
        if not user_obj:
            raise forms.ValidationError(_("Invalid %(value)s"), code='invalid', params={'value': 'Nickname'})
        else:
            if not user_obj.check_password(password):
                raise forms.ValidationError(_("Invalid %(value)s"), code='invalid',
                                            params={'value': 'Password'})
        return super().clean(*args, **kwargs)


class SignupForm(UserCreationForm):
    error_css_class = 'error'
    required_css_class = 'required'
    Choices = College_list
    nickname = forms.CharField(label='Nickname', max_length=20, help_text='Required')
    email = forms.EmailField(label='Email', max_length=70, help_text='Enter a valid Email Address', )
    college = forms.ChoiceField(label="select your college", choices=Choices)
    id_proof = forms.ImageField(label="Upload your I'd card", )

    class Meta:
        model = User
        fields = ('nickname', 'email', 'college', 'id_proof', 'password1', 'password2')


class UserView(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']


class UserDataView(forms.ModelForm):
    profile_pic = forms.ImageField(label=_('Profile Pic'), required=False, widget=forms.FileInput)

    class Meta:
        model = UserData
        fields = ['profile_pic',
                  'college',
                  'about']
