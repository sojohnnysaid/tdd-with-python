from django.contrib.auth.backends import ModelBackend


from accounts.models import User, Token


class PasswordlessAuthenticationBackend(ModelBackend):
    
    def authenticate(self, request, **kwargs):
        token = None
        try:
            uid = kwargs['password']
            token= Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            return User.objects.create(email=token.email)
        except KeyError: # token will not be found
            return None
        