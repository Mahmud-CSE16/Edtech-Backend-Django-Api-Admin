from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from common.models import Category, SubCategory, Chapter, QuestionHistory, Board, QuestionType
from common.api.serializers import  CategorySerializer, SubCategorySerializer ,ChapterSerializer, QuestionHistorySerializer, BoardSerializer, QuestionTypeSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]


class SubCategoryListAPIView(ListAPIView):
    queryset = SubCategory.objects.all().order_by("name")
    serializer_class = SubCategorySerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend,]
    filterset_fields = ['category',]


class ChapterListAPIView(ListAPIView):
    queryset = Chapter.objects.all().order_by("name")
    serializer_class = ChapterSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend,]
    filterset_fields = ['subcategory',]


class BoardListAPIView(ListAPIView):
    queryset = Board.objects.all().order_by('name')
    serializer_class = BoardSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend,]
    filterset_fields = ['subcategory',]


class QuestionHistoryListAPIView(ListAPIView):
    queryset = QuestionHistory.objects.all().order_by('-year')
    serializer_class = QuestionHistorySerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend,]
    filterset_fields = ['year','board',]
    search_fields = ['board__subcategory__name',]

class QuestionTypeListAPIView(ListAPIView):
    queryset = QuestionType.objects.all().order_by('name')
    serializer_class = QuestionTypeSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    