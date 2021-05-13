from django.contrib import admin
from django.contrib.admin import register

from .models import Like


class LikeTabularInline(admin.TabularInline):
    model = Like


@register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_filter = ('post', 'liked_at')
    list_display = ('post', 'liked_user', 'liked_at')

    ordering = ['liked_at']
    list_per_page = 50
    date_hierarchy = 'liked_at'
