from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from projects.models import Issue, Project
from projects.permissions import IsIssueCreatorOrReadOnly
from projects.serializers import IssueSerializer
from users.models import ProjectContributor
from drf_spectacular.utils import extend_schema


class IssueListPagination(PageNumberPagination):
    page_size = 30


@extend_schema(tags=["issues"])
class IssueListCreateView(generics.ListCreateAPIView):
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = IssueListPagination

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        return Issue.objects.filter(project__id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get("project_id")
        project = Project.objects.get(id=project_id)
        if not ProjectContributor.objects.filter(
            project=project, contributor=self.request.user
        ).exists():
            raise permissions.PermissionDenied(
                "You are not a contributor of this project."
            )
        serializer.save(created_by=self.request.user, project=project)


@extend_schema(tags=["issues"])
class IssueDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated, IsIssueCreatorOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Issue.objects.filter(project__contributors=user)

    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj
