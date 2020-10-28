from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .import models


@admin.register(models.User)
class ReceptionistUserAdmin(UserAdmin):
    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "gender",
                    "bio",
                    "superhost"
                )
            }
        ),
    )

    # list_filter = UserAdmin.list_display + ("superhost",)
    list_filter = ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "gender",
        "superhost",
        "created_at"
    )
