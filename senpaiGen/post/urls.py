from django.urls import path
from .views import LoadPost, AddPost


urlpatterns = [
    path('data/<int:no_of_posts>/', LoadPost.as_view(), name="post_data"),
    path('add_post', AddPost.as_view(), name="add_post")
]