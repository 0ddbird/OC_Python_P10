from django.urls import path

from comments.views import CommentDetailUpdateDeleteView, CommentListCreateView

urlpatterns = [
    path(
        "<int:project_id>/issues/<int:pk>/comments/",
        CommentListCreateView.as_view(),
        name="comment-list-create",
    ),
    path(
        "<int:project_id>/issues/<int:issue_id>/comments/<int:pk>/",
        CommentDetailUpdateDeleteView.as_view(),
        name="comment-detail-update-delete",
    ),
]
