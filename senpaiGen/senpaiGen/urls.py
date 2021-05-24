"""Main urls.py"""

from django.contrib import admin
from django.urls import path, include
from .import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

urlpatterns = [
    path('admin_plus_ultra/', admin.site.urls),  # Changed the path to admin for security purposes
    path('users/', include('django.contrib.auth.urls'),),
    path('', include('users.urls')),
    path('', include('like.urls')),  # To track likes
    path('', include('comments.urls')),
    path('', include('post.urls')),  # To load post data via ajax

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)


admin.site.site_header = "Senpai Gen"
admin.site.site_title = "Senpai Gen admin"
admin.site.index_title = "サイト管理"
