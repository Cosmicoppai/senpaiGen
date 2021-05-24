from django.urls import path
from .views import load_post


urlpatterns = [
    path('data/<int:no_of_posts>/', load_post, name="post_data"),
]