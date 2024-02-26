from rest_framework import serializers

from issues.models import Issue
from projects.models import Project


class IssueSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.username", read_only=True)

    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = [
            "created_by",
            "project",
            "created_time",
        ]

    def validate(self, data):
        project_id = self.context.get("project_id")
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            raise serializers.ValidationError({"project": "Project not found."})

        assigned_to = data.get("assigned_to")
        if assigned_to and not project.contributors.filter(id=assigned_to.id).exists():
            raise serializers.ValidationError(
                {"assigned_to": "This user is not a contributor of the project."}
            )

        return super().validate(data)
