from django.contrib import admin

from .models import Comment, Issue, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "created_at",
        "updated_at",
        "created_by",
    )
    search_fields = ("name", "description")


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "priority",
        "tag",
        "assigned_to",
        "created_by",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "status",
        "priority",
        "tag",
        "project",
    )
    search_fields = (
        "title",
        "description",
    )

    readonly_fields = ("project_id_display",)

    fields = (
        "title",
        "status",
        "priority",
        "tag",
        "assigned_to",
        "project_id_display",
    )

    def project_id_display(self, obj):
        if obj and obj.project_id:
            return obj.project.id
        return "N/A"

    project_id_display.short_description = "Project ID"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "issue", "created_by", "created_at")
    search_fields = ("text", "issue__title")
    list_filter = ("created_at", "created_by")
