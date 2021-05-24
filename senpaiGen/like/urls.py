from django.urls import path
from . import views

urlpatterns = [path('post/like/', views.add_like, name='like_counter'),


]