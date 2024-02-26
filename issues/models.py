from django.db import models

from projects.models import Project


class Issue(models.Model):
    STATUS_CHOICES = [
        ("todo", "To do"),
        ("progress", "In progress"),
        ("finished", "Finished"),
    ]

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    TAG_CHOICES = [
        ("bug", "Bug"),
        ("task", "Task"),
        ("enhancement", "Enhancement"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default="medium"
    )
    tag = models.CharField(max_length=15, choices=TAG_CHOICES, default="task")
    assigned_to = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_issues",
    )
    created_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="created_issues"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
