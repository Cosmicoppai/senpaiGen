from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView,  ListView
from .models import Post
from .forms import AddPostForm


class HomeView(LoginRequiredMixin, CreateView):  # To render html, js files and to create new post
    model = Post
    form_class = AddPostForm
    template_name = 'home.html'
    success_url = '/'

    """
    Below 'get' method will render the 'home.html' along with form(to create post) and necessary .js files to handle
     post load and other functions
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', context={'form': AddPostForm(self.request.POST or None, self.request.FILES or None)})

    """
    Below 'post' function is will create new post (the data is coming from the 'AddPostForm') and return the Json Response
     depending on wether the process is successfully completed or not.
     
     Go Beyond PlUS ULTRA
    """

    def post(self, request, *args, **kwargs):  # To create post 'form().is_valid()' can be call from here
        form = AddPostForm(self.request.POST or None, self.request.FILES or None)
        if self.request.method == "POST":
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.author = self.request.user
                new_post.save()
                data = {'error': False}
                return JsonResponse({'data':data})
            data = {'error': True, 'form_error': ''}
            return JsonResponse({'data':data})



class LoadPost(LoginRequiredMixin, ListView):  # To load(get) posts

    """
    Below 'get' function will extract 'no_of_post'(how many posts have to be loaded) from the url and will return
    the post data in Json Response
    """

    def get(self, request, *args, **kwargs):  # It'll take a request argument and a how many posts have to be loaded
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