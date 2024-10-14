from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User, Group

from .models import UserProfile


class ProfileInline(admin.StackedInline):
    "Profile inline for user model"
    model = UserProfile

class UserAdmin(AuthUserAdmin):
    "Base user's admin panel"
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(User, UserAdmin)
