from django.urls import path
from . import views

urlpatterns = [path('post/like/<int:pk>/', views.add_like, name='like_counter'),


]