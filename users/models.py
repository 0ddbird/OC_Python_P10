from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
    birthdate = models.DateField()


class ProjectContributor(models.Model):
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    contributor = models.ForeignKey("users.User", on_delete=models.CASCADE)
