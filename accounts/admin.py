from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "name",
        "is_staff",
    ]
    fieldsets = ((None, {"fields": ("name",)}),)
    add_fieldsets = ((None, {"fields": ("username", "password1", "password2")}),)
    
    #exclude = ("usable password",)


admin.site.register(CustomUser, CustomUserAdmin)