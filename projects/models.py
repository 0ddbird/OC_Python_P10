from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    contributors = models.ManyToManyField(
        "users.User", through="users.ProjectContributor", related_name="projects"
    )

    def __str__(self):
        return self.name
