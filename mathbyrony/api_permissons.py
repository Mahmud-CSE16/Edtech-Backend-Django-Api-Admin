from django.conf import settings

from rest_framework.permissions import BasePermission

class Check_API_KEY_Auth(BasePermission):
    def has_permission(self, request, view):
        try:
            # print(request.META['HTTP_API_KEY'])
            # API_KEY should be in request headers to authenticate requests
            api_key_secret = request.META['HTTP_API_KEY']
            return api_key_secret == settings.API_KEY_SECRET
        except:
            return False