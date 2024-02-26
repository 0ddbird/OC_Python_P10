# Generated by Django 5.0.1 on 2024-02-29 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Issue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("todo", "To do"),
                            ("progress", "In progress"),
                            ("finished", "Finished"),
                        ],
                        default="todo",
                        max_length=10,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("low", "Low"),
                            ("medium", "Medium"),
                            ("high", "High"),
                        ],
                        default="medium",
                        max_length=10,
                    ),
                ),
                (
                    "tag",
                    models.CharField(
                        choices=[
                            ("bug", "Bug"),
                            ("task", "Task"),
                            ("enhancement", "Enhancement"),
                        ],
                        default="task",
                        max_length=15,
                    ),
                ),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                ("updated_time", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]