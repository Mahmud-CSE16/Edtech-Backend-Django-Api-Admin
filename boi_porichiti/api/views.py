from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from mathbyrony.api_permissons import Check_API_KEY_Auth
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from common.models import SubCategory, QuestionHistory
# from common.api.serializers import  SubCategorySerializer, QuestionTypeSerializer
from boi_porichiti.models import Boi
from boi_porichiti.api.serializers import BoiSerializer


# bigoto bochor list view api 
class BoiListAPIView(ListAPIView):
    queryset = Boi.objects.all().order_by('title')
    serializer_class = BoiSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated & Check_API_KEY_Auth,]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend,]
    filterset_fields = ['subcategories',]
    search_fields = ('title',)