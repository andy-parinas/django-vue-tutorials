from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import AppUser

class AppUserAdmin(UserAdmin):
    model = AppUser
    list_display = ['email', 'username', 'is_staff']

admin.site.register(AppUser, AppUserAdmin)
