from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        "id",
        "username",
        "email",
        "can_be_contacted",
        "can_data_be_shared",
        "birthdate",
    ) + UserAdmin.list_display

    fieldsets = UserAdmin.fieldsets + (
        (
            "Informations supplémentaires",
            {"fields": ("can_be_contacted", "can_data_be_shared", "birthdate")},
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("can_be_contacted", "can_data_be_shared", "birthdate")}),
    )
