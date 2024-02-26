from rest_framework import serializers

from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.username", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = [
            "created_by",
            "issue",
            "created_time",
            "uuid",
        ]
