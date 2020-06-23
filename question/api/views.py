from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from question.models import Question
from question.api.serializers import QuestionSerializer


# get single question 
@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def question_api_view(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = QuestionSerializer(question)
        return Response(serializer.data)


# question list view api 
class QuestionListAPIView(ListAPIView):
    queryset = Question.objects.all().filter(published=True).order_by("?")
    serializer_class = QuestionSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend,]
    filterset_fields = ['subcategories','chapters','language','histories','types',]
    search_fields = ('subcategories__name','chapters__name','language__name','histories__board__name','histories__year','types__name',)

     
