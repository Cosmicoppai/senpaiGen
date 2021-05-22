from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Post


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    fields = ['title', 'body', 'image', 'author', 'date_added']