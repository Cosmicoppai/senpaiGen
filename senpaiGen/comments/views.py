from django.shortcuts import render
from django.views.generic import ListView
from .models import Comments
from users.models import User


class Comment(ListView):
    model = Comments
    template_name = 'home.html'
    # context_object_name = 'comments'
    ordering = 'added_at'


    '''def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nickname'] = User.nickname
        return context'''
