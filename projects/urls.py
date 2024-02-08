from django.urls import path

from projects.views.comment_views import (
    CommentDetailUpdateDeleteView,
    CommentListCreateView,
)
from projects.views.issue_views import IssueDetailUpdateDeleteView, IssueListCreateView
from projects.views.project_views import (
    AddContributorView,
    ProjectCreateView,
    ProjectDetailUpdateDeleteView,
)

urlpatterns = [
    path(
        "<int:project_id>/add_contributor/",
        AddContributorView.as_view(),
        name="add_contributor",
    ),
    path("create/", ProjectCreateView.as_view(), name="project-create"),
    path("<int:pk>/", ProjectDetailUpdateDeleteView.as_view(), name="project-detail"),
    path(
        "<int:project_id>/issues/create/",
        IssueListCreateView.as_view(),
        name="issue-list-create",
    ),
    path(
        "<int:project_id>/issues/<int:issue_id>/",
        IssueDetailUpdateDeleteView.as_view(),
        name="issue-detail-update-delete",
    ),
    path(
        "<int:project_id>/issues/<int:issue_id>/comments/",
        CommentListCreateView.as_view(),
        name="comment-list-create",
    ),
    path(
        "<int:project_id>/issues/<int:issue_id>/comments/<int:pk>/",
        CommentDetailUpdateDeleteView.as_view(),
        name="comment-detail-update-delete",
    ),
]
