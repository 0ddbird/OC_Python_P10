from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from django.core.cache import cache
from issues.models import Issue
from projects.models import Project
from issues.permissions import IsProjectContributor, IsIssueCreatorOrReadOnly
from issues.serializers import IssueSerializer


class IssueListPagination(PageNumberPagination):
    page_size = 30


@extend_schema(tags=["issues"])
class IssueListCreateView(generics.ListCreateAPIView):
    serializer_class = IssueSerializer
    permission_classes = [IsProjectContributor]
    pagination_class = IssueListPagination

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["project_id"] = self.kwargs["project_id"]
        return context

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        cache_key = f"issue_list_{project_id}"
        cached_issues = cache.get(cache_key)
        if cached_issues is not None:
            return cached_issues
        issues = Issue.objects.filter(project__id=project_id)
        cache.set(cache_key, issues, 3600)
        return issues

    def perform_create(self, serializer):
        project_id = self.kwargs.get("project_id")
        project = Project.objects.get(id=project_id)
        serializer.save(created_by=self.request.user, project=project)
        cache.delete(f"issue_list_{project_id}")


@extend_schema(tags=["issues"])
class IssueDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated, IsIssueCreatorOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["project_id"] = self.kwargs["project_id"]
        return context

    def get_queryset(self):
        user = self.request.user
        return Issue.objects.filter(project__contributors=user).select_related(
            "created_by", "project"
        )

    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_update(self, serializer):
        super().perform_update(serializer)
        project_id = serializer.instance.project_id
        cache.delete(f"issue_list_{project_id}")

    def perform_destroy(self, instance):
        project_id = instance.project_id
        super().perform_destroy(instance)
        cache.delete(f"issue_list_{project_id}")
