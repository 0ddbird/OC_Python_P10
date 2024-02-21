from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics
from users.serializers import UserSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

User = get_user_model()


def set_token_response(user=None, access_token=None):
    response = HttpResponse("Token set", status=200)
    if user:
        refresh = RefreshToken.for_user(user)
        response.set_cookie(
            "refresh_token",
            str(refresh),
            httponly=True,
            secure=False,
            samesite="None",
        )
        access_token = str(refresh.access_token)
    if access_token:
        response.set_cookie(
            "access_token",
            access_token,
            httponly=True,
            secure=False,
            samesite="None",
        )
    return response


class UserListPagination(PageNumberPagination):
    page_size = 10


class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return set_token_response(user)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class DeleteUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = UserListPagination

    def get_queryset(self):
        return User.objects.all().order_by("date_joined")


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise TokenError(e.args[0])

        user = serializer.user
        return set_token_response(user)


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")

        if refresh_token:
            data = {"refresh": refresh_token}
            request.data.update(data)

        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get("access")
            return set_token_response(access_token=access_token)
        return response
