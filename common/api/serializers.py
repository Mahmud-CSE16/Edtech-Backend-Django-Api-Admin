from rest_framework import serializers
from common.models import Board, Category, Chapter, QuestionHistory, SubCategory, QuestionType

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SubCategorySerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True,)

    class Meta:
        model = SubCategory
        fields = ['id','name','category',]

class ChapterSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(read_only=True,)

    class Meta:
        model = Chapter
        fields = ['id','name','number','subcategory']

class BoardSerializer(serializers.ModelSerializer):

    subcategory = SubCategorySerializer(read_only=True,)

    class Meta:
        model = Board
        fields = ['id','name','subcategory',]


class QuestionHistorySerializer(serializers.ModelSerializer):

    board = BoardSerializer(read_only=True,)

    class Meta:
        model = QuestionHistory
        fields = ['id','year','board']

class QuestionTypeSerializer(serializers.ModelSerializer):
     class Meta:
         model = QuestionType
         fields = "__all__"