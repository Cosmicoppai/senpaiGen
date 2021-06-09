from django.urls import path
from . import views

urlpatterns = [path('post/comment/', views.AddComment.as_view(), name='add_comment'),
               path('comment/<int:pk>/<int:no_of_comments>', views.Comment.as_view(), name='get_comments'),
               ]
