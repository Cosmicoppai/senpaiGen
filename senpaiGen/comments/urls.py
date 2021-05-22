from django.urls import path
from . import views

urlpatterns = [path('post/comment<int:pk>/', views.comment_add_form, name='add_comment'),
]