from drf_spectacular.extensions import OpenApiAuthenticationExtension
from rest_framework_simplejwt.authentication import JWTAuthentication


class JWTAuthSupportCookie(JWTAuthentication):
    """
    Extend the JWTAuthentication class to support cookie based authentication.
    """

    def authenticate(self, request):
        raw_token = request.COOKIES.get("access_token")
        if raw_token is not None:
            validated_token = self.get_validated_token(raw_token)
            return self.get_user(validated_token), validated_token
        return super().authenticate(request)


class JWTAuthSupportCookieExtension(OpenApiAuthenticationExtension):
    target_class = "users.authentication.JWTAuthSupportCookie"
    name = "JWTAuthSupportCookie"

    def get_security_definition(self, auto_schema):
        description = (
            "L'authentification est effectuée via des cookies HTTP only. "
            "Assurez-vous d'envoyer l'access_token et le refresh_token "
            "dans les cookies de votre requête. Ce schéma est utilisé uniquement "
            "à des fins de documentation et ne reflète pas directement le mécanisme "
            "d'envoi de token."
        )
        return {
            "type": "http only cookies",
            "in": "cookies",
            "name": "access_token",
            "description": description,
        }
