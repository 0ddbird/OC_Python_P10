from rest_framework import permissions

from projects.models import Project


class IsProjectContributor(permissions.BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs.get("project_id")
        if project_id:
            try:
                project = Project.objects.get(id=project_id)
                return project.contributors.filter(id=request.user.id).exists()
            except Project.DoesNotExist:
                return False
        return False

    def has_object_permission(self, request, view, obj):
        return obj.project.contributors.filter(id=request.user.id).exists()


class IsIssueCreatorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.created_by == request.user
