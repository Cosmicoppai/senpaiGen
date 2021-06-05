from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Comments
from .forms import CommentForm
from post.models import Post
from django.utils.translation import gettext as _


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
                except ObjectDoesNotExist or AttributeError:
                    messages.error(request, _('Unable to add Comment'))
            messages.error(request, _('Try again later'))  # Later edit this message
        return render(request, 'comments.html', {'commentform': form})

    return HttpResponseRedirect("/")
