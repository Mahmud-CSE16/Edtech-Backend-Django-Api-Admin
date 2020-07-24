from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from mathbyrony.api_permissons import Check_API_KEY_Auth
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from notification.models import Notification
from notification.api.serializers import NotificationSerializer

# question list view api 
class NotificationListAPIView(ListAPIView):
    queryset = Notification.objects.all().filter(published=True).order_by('published_time')
    serializer_class = NotificationSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated & Check_API_KEY_Auth,]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend,]
    filterset_fields = ['subcategories',]
    search_fields = ('title',)
