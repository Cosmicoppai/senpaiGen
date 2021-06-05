from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate
from django.http import HttpResponseRedirect
from .forms import LoginForm, SignupForm
from django.utils.translation import gettext as _
from django.contrib import messages
from .forms import UserView, UserDataView
from post.views import HomeView

# User Model (AbstractBaseUser)
User = get_user_model()


def home_view(request):
    if request.user.is_authenticated:
        return HomeView.as_view()(request)  # Home page with list of post
        # return redirect('post:PostListView')
    return user_login(request)


def signup(request):
    if request.user.is_authenticated:
        return HomeView.as_view()(request)
    form = SignupForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()  # load the profile instance created by the signal

        # set the processed 'college name' to the college of user
        user.userdata.college = form.cleaned_data.get('college')

        # set the processed 'id_proof' to the id_proof of user
        user.userdata.id_proof = form.cleaned_data.get('id_proof')
        # user.save()
        user.userdata.save()  # save the userdata model after setting all the required fields
        messages.success(request, _('Your account has been created successfully'))
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=user.nickname, password=raw_password)
        login(request, user)
        return redirect('home')
    return render(request, 'signUp.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return HomeView.as_view()(request)
    form = LoginForm(request.POST or None)
    if form.is_valid():
        nickname = form.cleaned_data.get('nickname')
        user_obj = User.objects.get(nickname__iexact=nickname)
        login(request, user_obj)
        return HttpResponseRedirect("/")
    return render(request, "login.html", {"form": form})


# Logout is covered by django.contrib.auth.urls
'''def user_logout(request, *args, **kwargs):
    logout(request)'''


@login_required
def EditProfile(request, pk):
    user = User.objects.get(pk=pk)
    userform = UserView(instance=user)
    userdataform = UserDataView(instance=user.userdata)

    if request.user.is_authenticated and request.user.id == user.id:
        if request.method == 'POST':
            userform = UserView(request.POST, instance=user)
            userdataform = UserDataView(request.POST, request.FILES, instance=user.userdata)
            if userform.has_changed() or userdataform.has_changed():
                if userform.is_valid() and userdataform.is_valid():
                    updated_user = userform.save(commit=False)
                    updated_user.user = request.user
                    updated_user.save()
                    updated_user.userdata.profile_pic = userdataform.cleaned_data.get('profile_pic')
                    updated_user.userdata.college = userdataform.cleaned_data.get('college')
                    updated_user.userdata.about = userdataform.cleaned_data.get('about')
                    updated_user.userdata.save()

                    messages.success(request, _('Profile Updated Successfully'))
                    return redirect(EditProfile, pk=pk,)
        return render(request, 'profile_view.html', {'pk': pk,
                                                     'userform': userform,
                                                     'userdataform': userdataform})
    raise PermissionDenied


# class
