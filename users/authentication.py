from rest_framework_simplejwt.authentication import JWTAuthentication


class JWTAuthSupportCookie(JWTAuthentication):
    """
    Extend the JWTAuthentication class to support cookie based authentication.
    """

    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            raw_token = request.COOKIES.get("access_token")
            if raw_token is not None:
                validated_token = self.get_validated_token(raw_token)
                return self.get_user(validated_token), validated_token
        else:
            return super().authenticate(request)
