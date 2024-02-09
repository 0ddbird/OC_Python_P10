from rest_framework import serializers

from projects.models import Comment, Issue, Project
from users.models import ProjectContributor


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "description", "created_by"]
        read_only_fields = ["created_by"]


class ProjectContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectContributor
        fields = ["project", "contributor"]


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = ["created_by", "project"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
