from django.contrib import admin

from .models import Thumbnail

# Register your models here.


@admin.register(Thumbnail)
class Thumbnaildmin(admin.ModelAdmin):
    list_display = (
        "url",
        "max_height",
        "max_width",
        "image",
    )
    search_fields = ("url", "max_height", "max_width")
    readonly_fields = ("created", "modified")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "url",
                    "max_height",
                    "max_width",
                    "image",
                )
            },
        ),
        ("Metadata", {"fields": ("created", "modified"), "classes": ("collapse",)}),
    )
    ordering = ("-created",)
    date_hierarchy = "created"
