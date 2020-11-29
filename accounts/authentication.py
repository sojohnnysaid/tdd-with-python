from django.contrib.auth.backends import ModelBackend
from accounts.models import User, Token


class PasswordlessAuthenticationBackend(ModelBackend):
    
    def authenticate(self, uid, request=None):
        token = None
        try:
            token= Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            return User.objects.create(email=token.email)
        except Token.DoesNotExist:
            return None

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None