from django.urls import path

from projects.views import (
    AddContributorView,
    ProjectDetailUpdateDeleteView,
    ProjectListCreateView,
)

urlpatterns = [
    path(
        "<int:project_id>/add_contributor/",
        AddContributorView.as_view(),
        name="add_contributor",
    ),
    path("", ProjectListCreateView.as_view(), name="project-list-create"),
    path("<int:pk>/", ProjectDetailUpdateDeleteView.as_view(), name="project-detail"),
]
