from django.contrib import admin
from django.db import OperationalError
from .models import Account, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

# Register your models here.

class AccountAdmin(UserAdmin):
    try:
        list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
        readonly_fields = ('last_login', 'date_joined')
        ordering = ('date_joined',)
        list_display_links = ('email', 'first_name', 'last_name')

        filter_horizontal = ()
        list_filter = ()
        fieldsets = ()

    except OperationalError:
        pass

class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('user', 'city', 'state', 'country')

admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)