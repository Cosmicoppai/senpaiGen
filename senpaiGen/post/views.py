# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import CreateView
from django.views import View
from .models import Post
from .forms import AddPostForm


class HomeView(LoginRequiredMixin, CreateView):  # To create new post

    model = Post
    form_class = AddPostForm
    template_name = 'home.html'
    context_object_name = 'postForm'
    success_url = '/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return HttpResponseRedirect(self.success_url)



class LoadPost(LoginRequiredMixin, View):


    @staticmethod
    def get(request, **kwargs):  # It'll take a request argument and a how many posts have to be loaded
        no_of_posts = kwargs['no_of_posts']
        visible = 3
        upper_limit = no_of_posts
        lower_limit = upper_limit - visible
        qs = Post.objects.all().order_by('-id')[lower_limit:upper_limit]  # Query the database and load the latest 3 post
        size = qs.count()  # if size is less than 'visible' scipt.js will hide the 'lOAD MORE POSTS BUTTON'
        data = []
        for obj in qs:
            try:
                image_ = obj.image.url
            except ValueError:
                image_ = None  # When there is no image attached with the post

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