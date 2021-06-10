from django.urls import path
from .views import LoadPost, HomeView, post_list_on_userProfile


urlpatterns = [
    path('data/<int:no_of_posts>/', LoadPost.as_view(), name="post_data"),
    path('new_post', HomeView.as_view(), name="add_post"),
    path('post_list/<int:no_of_posts>/<str:author>', post_list_on_userProfile, name="post_list_on_userProfile")
]