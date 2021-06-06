from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Comments
from .forms import CommentForm
from post.models import Post
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin


class Comment(ListView):
    # model = Comments
    # ordering = '-added_at'

    def get(self, request, *args, **kwargs):
        visible = 4
        upper_limit = kwargs['no_of_comments']
        lower_limit = upper_limit - visible
        post_ = Post.objects.get(pk=kwargs['pk'])
        qs = Comments.objects.filter(post=post_).order_by('-added_at')[lower_limit:upper_limit]
        data = []
        size = qs.count()
        for obj in qs:
            item = {'comment': obj.comment,
                    'author': obj.author.nickname,
                    'date_added': obj.added_at.strftime("%d %b %Y "),
                    }
            data.append(item)
        return JsonResponse({'data': data, 'size': size})



class AddComment(LoginRequiredMixin, CreateView):
    model = Comments
    form_class = CommentForm
    template_name = 'comments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addCommentForm'] = self.get_form()  # similar as context['add-comment-form'] = context['form']
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                new_comment = form.save(commit=False)
                post_ = Post.objects.get(pk=kwargs['pk'])
                new_comment.post = post_
                new_comment.author = self.request.user
                new_comment.save()
                messages.success(request, _('Comment added Successfully'))
                return HttpResponseRedirect("/")
            messages.error(request, _('Try Again Later'))
            return HttpResponseRedirect('/')
