from django.contrib import admin

from issues.models import Issue


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "status",
        "priority",
        "tag",
        "assigned_to",
        "created_by",
        "created_time",
        "updated_time",
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

    readonly_fields = (
        "project_id_display",
        "created_time",
        "updated_time",
    )

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
