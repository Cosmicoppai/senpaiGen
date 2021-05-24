from django.core.exceptions import ObjectDoesNotExist
from .models import Like
from post.models import Post
from django.http import JsonResponse


def add_like(request):

    if request.is_ajax():

        pk = request.POST.get('pk')
        if pk is None:
            return JsonResponse({'error': 'Invalid Post'})

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
            # return HttpResponseRedirect("/")
            return JsonResponse({'status':200, 'total_no_of_likes':post_.total_no_of_likes, 'msg':'Like'})

        else:
            obj = Like(liked_user=request.user, post=post_, like=1)
            obj.save()
            # return HttpResponseRedirect("/")
            return JsonResponse({'status':200, 'total_no_of_likes':post_.total_no_of_likes+1, 'msg':'Unlike'})