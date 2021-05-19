"""Main urls.py"""

from django.contrib import admin
from django.urls import path, include, re_path
from .import settings
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from users.views import home_view, user_login, signup, ProfileView
from like.views import add_like

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls'),),
    # path('', PostListView.as_view(), name='home'),
    path('', home_view, name='home'),
    re_path(r'^login/$', user_login, name='login'),
    re_path(r'^signup/$', signup, name='signup'),
    # url(r'^logout/$', user_logout, name='logout'),
    path('profile/<int:pk>/', ProfileView, name='ProfileView'),
    path('post/like/<int:pk>/', add_like, name='like_counter')

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)


admin.site.site_header = "Senpai Gen"
admin.site.site_title = "Senpai Gen admin"
admin.site.index_title = "サイト管理"
