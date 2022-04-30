from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": ("country", "date", "title_kr", "category", "sector",)
            },
        ),
        (
            "Contents",
            {
                "fields": ("content_kr", "reference", "link",)
            },
        ),
    )

    list_display = ("country", "date", "title_kr", "category", "sector", "reference", "link",
        
    )

    list_filter = (
        "category",
        "sector",
        "country",
    )

    search_fields = ["country", "title_kr", "reference"]