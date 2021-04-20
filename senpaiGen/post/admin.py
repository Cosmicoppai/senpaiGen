from django.contrib import admin
from .models import Post
from django.contrib.admin import register
from comments.admin import CommentTabularInline


class PostTabularInline(admin.TabularInline):
    model = Post


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_added')
    list_filter = ('title', 'author', 'date_added')
    search_fields = ('author', 'title')
    ordering = ['date_added']
    date_hierarchy = 'date_added'
    inlines = [CommentTabularInline]


