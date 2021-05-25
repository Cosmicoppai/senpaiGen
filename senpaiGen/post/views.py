from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Post


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    # fields = ['title', 'body', 'image', 'author', 'date_added']

    # def get(self):



@login_required
def load_post(request, no_of_posts):  # It'll take a request argument and a how many posts have to be loaded
    visible = 3
    upper_limit = no_of_posts
    lower_limit = upper_limit - visible
    # qs = Post.objects.all()  # query all the posts from database
    qs = Post.objects.all().order_by('-id')[lower_limit:upper_limit]
    size = qs.count()  # Correct the error,  cuz of it only 3 posts are loading in the view
    data = []
    for obj in qs:
        try:
            image_ = obj.image.url
        except ValueError:
            image_ = None  # When there is no image with the post

        item = {
            'id':obj.id,
            'title':obj.title,
            'body':obj.body,
            'image':image_,
            'liked': True if obj.likes.filter(liked_user=request.user).count() > 0 else False,
            'like_count': obj.total_no_of_likes,
            'comment_count': obj.comments.all().count(),
            'author': obj.author.nickname,
            'date': obj.date_added.strftime("%d %b %Y "),  # To convert the datetime object into string

        }
        data.append(item)
    return JsonResponse({'data': data, 'size':size})