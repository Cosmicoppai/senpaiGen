from django.urls import path, re_path
from . import views

urlpatterns = [path('', views.home_view, name='home'),
               # path('', PostListView.as_view(), name='home'),
               re_path(r'^login/$', views.user_login, name='login'),
               re_path(r'^signup/$', views.signup, name='signup'),
               # url(r'^logout/$', user_logout, name='logout'),
               path('profile/<int:pk>/', views.ProfileView, name='EditProfile'),  # If a user wants to edit his profile
               path('user/<int:pk>', views.ProfileView, name='ProfileView'),  # If a one user wants to see another user profile

               ]
