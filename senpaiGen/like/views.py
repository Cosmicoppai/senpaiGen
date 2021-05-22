from django.core.exceptions import ObjectDoesNotExist
from .models import Like
from post.models import Post
from django.http import HttpResponseRedirect


def add_like(request, pk):

    post_ = Post.objects.get(pk=pk)
    # a = Like.objects.filter(liked_user=request.user) & Like.objects.filter(post=post_)

    try:
        obj_ = Like.objects.get(liked_user=request.user, post=post_)  # check if already lik exist from current user or not .
    except ObjectDoesNotExist:
        obj_ = None

    if obj_:  # if the like from the current user exist on the same post
        obj_.delete()
        post_.total_no_of_likes -= 1
        post_.save()
        return HttpResponseRedirect("/")

    else:
        obj = Like(liked_user=request.user, post=post_, like=1)
        obj.save()
        return HttpResponseRedirect("/")