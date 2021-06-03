from django.urls import path
from .views import LoadPost


urlpatterns = [
    path('data/<int:no_of_posts>/', LoadPost.as_view(), name="post_data"),
]