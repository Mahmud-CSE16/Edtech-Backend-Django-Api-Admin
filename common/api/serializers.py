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
        fields = ['id','name','category','mark_of_correct_mcq_question','negative_mark_of_incorrect_question','number_of_questions_for_mcq_exam','time_in_minute',]

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