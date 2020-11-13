from django.contrib import admin
from . import models


class TemperatureInLine(admin.TabularInline):
    model = models.Temperature


@admin.register(models.Visitor)
class VisitorAdmin(admin.ModelAdmin):
    """ Visitor Admin """

    inlines = [TemperatureInLine, ]

    list_display = (
        "name",
        "email",
        "phone_number",
    )
