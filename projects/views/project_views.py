from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import Project
from projects.permissions import IsProjectContributor, IsProjectCreatorOrReadOnly
from projects.serializers import ProjectContributorSerializer, ProjectSerializer
from users.models import ProjectContributor


class ProjectListPagination(PageNumberPagination):
    page_size = 10


@extend_schema(tags=["projects"])
class AddContributorView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=ProjectContributorSerializer,
        responses={201: ProjectContributorSerializer},
    )
    def post(self, request, project_id):
        user = request.user
        project = get_object_or_404(Project, pk=project_id)

        if ProjectContributor.objects.filter(
            project=project, contributor=user
        ).exists():
            return Response(
                {"message": "You are already a contributor of this project."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = ProjectContributorSerializer(
            data={"project": project.id, "contributor": user.id}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["projects"])
class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = ProjectListPagination

    def get_queryset(self):
        return Project.objects.all().order_by("created_at")

    def perform_create(self, serializer):
        user = self.request.user
        project = serializer.save(created_by=user)
        ProjectContributor.objects.create(project=project, contributor=user)


@extend_schema(tags=["projects"])
class ProjectDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsProjectContributor, IsProjectCreatorOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(contributors=user)

    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj


@extend_schema(tags=["projects"])
class ContributorProjectsListView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsProjectContributor]
    pagination_class = ProjectListPagination

    def get_queryset(self):
        user = self.request.user
        return (
            Project.objects.filter(projectcontributor__contributor=user.id)
            .distinct()
            .order_by("created_at")
        )
