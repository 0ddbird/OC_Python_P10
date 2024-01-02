from django.db import models
from users.models import User


class Contributor(User):
    pass


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Contributor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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
        Contributor, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_by = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    text = models.TextField()
    created_by = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.created_by} on {self.created_at}"


