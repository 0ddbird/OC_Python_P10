from rest_framework import permissions


class IsAuthenticatedAndProjectContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.contributors.filter(id=request.user.id).exists()


class IsIssueCreatorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.created_by == request.user


class IsCommentCreatorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.created_by == request.user
