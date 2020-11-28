from django.contrib.auth.backends import ModelBackend
from accounts.models import User, Token


class PasswordlessAuthenticationBackend(ModelBackend):
    
    def authenticate(self, request, **kwargs):
        print('i was called')
        token = None
        try:
            uid = kwargs['uid']
            token= Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            return User.objects.create(email=token.email)
        except KeyError: # token will not be found
            return None

    def get_user(self, email):
        print('i was called too')
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None