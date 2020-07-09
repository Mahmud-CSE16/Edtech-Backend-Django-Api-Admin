from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from mathbyrony.api_permissons import Check_API_KEY_Auth
from common.models import Category, SubCategory, Chapter, QuestionHistory, Board, QuestionType
from common.api.serializers import  CategorySerializer, SubCategorySerializer ,ChapterSerializer, QuestionHistorySerializer, BoardSerializer, QuestionTypeSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all().order_by("name")
    permission_classes = [Check_API_KEY_Auth,]
    serializer_class = CategorySerializer


class SubCategoryListAPIView(ListAPIView):
    queryset = SubCategory.objects.all().order_by("name")
    serializer_class = SubCategorySerializer
    permission_classes = [Check_API_KEY_Auth,]
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend,]
    filterset_fields = ['category',]


class ChapterListAPIView(ListAPIView):
    queryset = Chapter.objects.all().order_by("name")
    serializer_class = ChapterSerializer
    permission_classes = [Check_API_KEY_Auth,]
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend,]
    filterset_fields = ['subcategory',]


class BoardListAPIView(ListAPIView):
    queryset = Board.objects.all().order_by('name')
    serializer_class = BoardSerializer
    permission_classes = [Check_API_KEY_Auth,]
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend,]
    filterset_fields = ['subcategory',]


class QuestionHistoryListAPIView(ListAPIView):
    queryset = QuestionHistory.objects.all().order_by('-year')
    serializer_class = QuestionHistorySerializer
    permission_classes = [Check_API_KEY_Auth,]
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend,]
    filterset_fields = ['year','board',]
    search_fields = ['board__subcategory__name',]

class QuestionTypeListAPIView(ListAPIView):
    queryset = QuestionType.objects.all().order_by('name')
    serializer_class = QuestionTypeSerializer
    permission_classes = [Check_API_KEY_Auth,]
    