import uuid

from django.db import models

from issues.models import Issue


class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    description = models.TextField()
    created_by = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    created_time = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"Comment by {self.created_by} on {self.created_time}"
