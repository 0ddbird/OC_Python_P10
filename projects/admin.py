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
    # Ajoutez project_id_display à readonly_fields pour l'afficher dans la vue de modification
    readonly_fields = ("project_id_display",)

    # Spécifiez les champs à inclure dans le formulaire, en omettant 'project_id' car vous avez 'project_id_display'
    fields = (
        "title",
        "status",
        "priority",
        "tag",
        "assigned_to",
        "project_id_display",  # Assurez-vous que ceci est inclus dans votre formulaire
    )

    def project_id_display(self, obj):
        # Vérifiez si obj est défini pour éviter des erreurs lors de la création de nouveaux objets
        if obj and obj.project_id:
            return obj.project.id
        return "N/A"  # Retournez une valeur par défaut pour les nouveaux objets

    project_id_display.short_description = "Project ID"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "issue", "created_by", "created_at")
    search_fields = ("text", "issue__title")
    list_filter = ("created_at", "created_by")
