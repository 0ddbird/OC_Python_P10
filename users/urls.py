from django.urls import path
from projects.views.project_views import ContributorProjectsListView

from users.views import (
    CreateUserView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    UserListView,
)

urlpatterns = [
    path("create/", CreateUserView.as_view(), name="create_user"),
    path("", UserListView.as_view(), name="user-list"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
    path(
        "projects/", ContributorProjectsListView.as_view(), name="contributor_projects"
    ),
]
