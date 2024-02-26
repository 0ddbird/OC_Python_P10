from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from django.core.cache import cache

from comments.models import Comment
from issues.models import Issue
from comments.permissions import IsProjectContributor, IsCommentCreatorOrReadOnly
from comments.serializers import CommentSerializer


class CommentListPagination(PageNumberPagination):
    page_size = 50


@extend_schema(tags=["comments"])
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsProjectContributor]
    pagination_class = CommentListPagination

    def get_queryset(self):
        issue_id = self.kwargs.get("pk")
        cache_key = f"comment_list_{issue_id}"
        cached_comments = cache.get(cache_key)
        if cached_comments is not None:
            return cached_comments
        comments = Comment.objects.filter(issue__id=issue_id).select_related(
            "created_by", "issue__project"
        )
        cache.set(cache_key, comments, 3600)
        return comments

    def perform_create(self, serializer):
        issue_id = self.kwargs.get("pk")
        issue = Issue.objects.get(id=issue_id)
        serializer.save(created_by=self.request.user, issue=issue)
        cache.delete(f"comment_list_{issue_id}")


@extend_schema(tags=["comments"])
class CommentDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsCommentCreatorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(issue__project__contributors=self.request.user)

    def perform_update(self, serializer):
        issue_id = serializer.instance.issue_id
        super().perform_update(serializer)
        cache.delete(f"comment_list_{issue_id}")

    def perform_destroy(self, instance):
        issue_id = instance.issue_id
        super().perform_destroy(instance)
        cache.delete(f"comment_list_{issue_id}")
