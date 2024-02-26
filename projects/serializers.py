from rest_framework import serializers

from projects.models import Project
from users.models import ProjectContributor


class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.username", read_only=True)

    class Meta:
        model = Project
        fields = ["id", "name", "description", "created_by", "created_time"]
        read_only_fields = [
            "created_by",
        ]


class ProjectContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectContributor
        fields = [
            "project",
            "contributor",
        ]
