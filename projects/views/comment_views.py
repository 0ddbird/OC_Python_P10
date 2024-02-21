from rest_framework import generics, permissions

from projects.models import Comment, Issue
from projects.permissions import (
    IsProjectContributor,
    IsCommentCreatorOrReadOnly,
)
from projects.serializers import CommentSerializer
from rest_framework.pagination import PageNumberPagination


class CommentListPagination(PageNumberPagination):
    page_size = 50


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [
        IsProjectContributor,
    ]
    pagination_class = CommentListPagination

    def get_queryset(self):
        issue_id = self.kwargs.get("pk")
        return Comment.objects.filter(issue__id=issue_id)

    def perform_create(self, serializer):
        issue_id = self.kwargs.get("pk")
        print(issue_id)
        issue = Issue.objects.get(id=issue_id)
        if not issue.project.contributors.filter(id=self.request.user.id).exists():
            raise permissions.PermissionDenied(
                "You are not a contributor of this project."
            )
        serializer.save(created_by=self.request.user, issue=issue)


class CommentDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsCommentCreatorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(issue__project__contributors=self.request.user)
