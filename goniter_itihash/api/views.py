from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from mathbyrony.api_permissons import Check_API_KEY_Auth
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from common.models import SubCategory, QuestionHistory
# from common.api.serializers import  SubCategorySerializer, QuestionTypeSerializer
from goniter_itihash.models import GoniterItihash
from goniter_itihash.api.serializers import GoniterItihashSerializer


# bigoto bochor list view api 
class GoniterItihashListAPIView(ListAPIView):
    queryset = GoniterItihash.objects.all().filter(published=True).order_by('title')
    serializer_class = GoniterItihashSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated & Check_API_KEY_Auth,]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend,]
    search_fields = ('title',)