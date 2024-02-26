from django.urls import path

from issues.views import IssueDetailUpdateDeleteView, IssueListCreateView

urlpatterns = [
    path(
        "<int:project_id>/issues/",
        IssueListCreateView.as_view(),
        name="issue-list",
    ),
    path(
        "<int:project_id>/issues/create/",
        IssueListCreateView.as_view(),
        name="issue-create",
    ),
    path(
        "<int:project_id>/issues/<int:pk>/",
        IssueDetailUpdateDeleteView.as_view(),
        name="issue-detail-update-delete",
    ),
]
