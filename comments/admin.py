from django.contrib import admin

from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uuid",
        "issue",
        "created_by",
        "created_time",
    )
    search_fields = (
        "description",
        "issue__title",
    )
    list_filter = (
        "issue",
        "created_by",
        "created_time",
    )
