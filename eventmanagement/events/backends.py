"""
    Cusrom Authentication for the EventMangement.

    EventMangement 2023.

    Author - Jay Chovatiya - Grewon Technologies Pvt Ltd
"""

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import CustomUser

class CustomUserAuthenticationBackend(BaseAuthentication):

    def authenticate(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email:
            raise AuthenticationFailed('Please enter valid email')
        if not password:
            raise AuthenticationFailed('Password is required.')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed('Invalid email, user not found!')

        if user.check_password(password):
            return user, None

        raise AuthenticationFailed('Invalid password, please enter password!')

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
