from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from mathbyrony.api_permissons import Check_API_KEY_Auth

from question.models import McqQuestion
from question.api.serializers import McqQuestionSerializer


# get single question 
@api_view(['GET',])
@permission_classes([IsAuthenticated&Check_API_KEY_Auth,])
def mcq_question_api_view(request, pk):
    try:
        question = McqQuestion.objects.get(pk=pk)
    except McqQuestion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = McqQuestionSerializer(question)
        return Response(serializer.data)

class DefaultResultsSetPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'size'
    max_page_size = 100

# question list view api 
class McqQuestionListAPIView(ListAPIView):
    queryset = McqQuestion.objects.all().filter(published=True).order_by("?")
    serializer_class = McqQuestionSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated & Check_API_KEY_Auth,]
    pagination_class = DefaultResultsSetPagination
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend,]
    filterset_fields = ['subcategories','chapters','language','histories','types',]
    search_fields = ('subcategories__name','chapters__name','language__name','histories__board__name','histories__year','types__name',)

     
