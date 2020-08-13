from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from mathbyrony.api_permissons import Check_API_KEY_Auth
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from common.models import SubCategory, QuestionHistory
# from common.api.serializers import  SubCategorySerializer, QuestionTypeSerializer
from bigoto_bochor.models import BigotoBochor
from bigoto_bochor.api.serializers import BigotoBochorSerializer


# bigoto bochor list view api 
class BigotoBochorListAPIView(ListAPIView):
    queryset = BigotoBochor.objects.all().order_by('-question_history__year')
    serializer_class = BigotoBochorSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated & Check_API_KEY_Auth,]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend,]
    filterset_fields = ['subcategory',]
    search_fields = ('subcategory','question_history__year','question_history__board')
