from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from projects.models import Project
from projects.permissions import IsAuthenticatedAndProjectContributor
from projects.serializers import ProjectContributorSerializer, ProjectSerializer
from users.models import ProjectContributor


class AddContributorView(APIView):
    permission_classes = [permissions.IsAuthenticated]

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


class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        project = serializer.save(created_by=user)
        ProjectContributor.objects.create(project=project, contributor=user)


class ProjectDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthenticatedAndProjectContributor,
    ]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(contributors=user)
