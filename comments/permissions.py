from rest_framework import permissions

from issues.models import Issue


class IsProjectContributor(permissions.BasePermission):
    def has_permission(self, request, view):
        issue_id = view.kwargs.get("pk")
        try:
            issue = Issue.objects.get(id=issue_id)
            project = issue.project
        except Issue.DoesNotExist:
            return False

        return project.contributors.filter(id=request.user.id).exists()

    def has_object_permission(self, request, view, obj):
        return obj.issue.project.contributors.filter(id=request.user.id).exists()


class IsCommentCreatorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.created_by == request.user
