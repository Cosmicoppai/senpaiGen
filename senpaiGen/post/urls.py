from django.urls import path
from .views import LoadPost, HomeView


urlpatterns = [
    path('data/<int:no_of_posts>/', LoadPost.as_view(), name="post_data"),
    path('new_post', HomeView.as_view(), name="add_post")
]