from django.urls import path, re_path
from . import views

urlpatterns = [path('', views.home_view, name='home'),
               # path('', PostListView.as_view(), name='home'),
               re_path(r'^login/$', views.user_login, name='login'),
               re_path(r'^signup/$', views.signup, name='signup'),
               # url(r'^logout/$', user_logout, name='logout'),
               path('profile/<int:pk>/', views.ProfileView.as_view(), name='ProfileView'),
               # If a user wants to see his profile
               path('profile-edit/<int:pk>', views.EditProfile, name='EditProfile'),  # If a one user wants to see another user profile

               # To temporarily redirect the user from profile/nickname to profile/user_id
               path('profile/<str:nickname>', views.ProfileRedirect.as_view(), name="profile_redirect")

               ]
