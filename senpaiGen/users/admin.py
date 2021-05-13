from django.contrib import admin
from .models import UserData
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from post.admin import PostTabularInline
from comments.admin import CommentTabularInline
from like.admin import LikeTabularInline

User = get_user_model()


# @admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ['nickname', 'email']
    list_filter = ['nickname', 'email']
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('nickname', 'email', 'password')}),
        ('Permission', {'fields': ('admin', 'staff', 'active')}),
        ('Important Dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('nickname', 'email', 'password1', 'password2')
                }),
    )

    search_fields = ('nickname', 'email',)
    ordering = ('nickname',)
    inlines = [PostTabularInline, CommentTabularInline, LikeTabularInline]



admin.site.register(User, UserAdmin)
admin.site.register(UserData)
admin.site.unregister(Group)
