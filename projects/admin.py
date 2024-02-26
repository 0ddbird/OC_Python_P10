from django.contrib import admin

from projects.models import Project


class ProjectContributorInline(
    admin.TabularInline
):  # Ou StackedInline pour une présentation différente
    model = Project.contributors.through
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "created_time",
        "updated_time",
        "created_by",
    )
    search_fields = ("name", "description")
    inlines = [ProjectContributorInline]
