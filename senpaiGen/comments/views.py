from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from .models import Comments
from .forms import CommentForm
from post.models import Post
from django.utils.translation import gettext as _


class Comment(ListView):
    model = Comments
    template_name = 'home.html'
    # context_object_name = 'comments'
    ordering = 'added_at'

    '''def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nickname'] = User.nickname
        return context'''


@login_required
def comment_add_form(request, pk):
    if request.user.is_authenticated:
        form = CommentForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                comment_ = form.cleaned_data.get('comment')
                post_ = Post.objects.get(pk=pk)
                try:
                    comment_obj = Comments(author=request.user, post=post_, comment=comment_)
                    comment_obj.save()
                    messages.success(request, _('Comment added Successfully'))
                    return HttpResponseRedirect("/")
                except:
                    messages.error(request, _('Unable to add Comment'))
            messages.error(request, _('Try again later'))
        return render(request, 'comments.html', {'commentform':form})

    raise PermissionDenied
