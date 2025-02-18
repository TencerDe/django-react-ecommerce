from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'city', 'state', 'phone_number', 'password1', 'password2')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

