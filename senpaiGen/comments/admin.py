from django.contrib import admin
from .models import Comments
from django.contrib.admin import register


class CommentTabularInline(admin.TabularInline):
    model = Comments


@register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'author', 'post')
    list_filter = ('comment', 'author', 'post')

    """underscore is for the foreign-key fields. ('yourforeignkeyname__choosefieldnameinyourforeignkey')
        yourforeignkeyname is the name of the field in the models.py of this app
        choosefieldnameinyourforeignkey is the name of the field in the foreignkey's models.py 
        (example:- 'nickname' in 'users')"""

    search_fields = ['comment', 'author__nickname', 'post__title']
    ordering = ['added_at']
    list_per_page = 50
    date_hierarchy = 'added_at'
