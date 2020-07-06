from django.urls import path

from common.api.views import CategoryListAPIView, SubCategoryListAPIView, ChapterListAPIView, BoardListAPIView, QuestionHistoryListAPIView, QuestionTypeListAPIView

app_name = 'common'

urlpatterns = [
    path('categories/',CategoryListAPIView.as_view(),name='categories'),
    path('subcategories/',SubCategoryListAPIView.as_view(),name='subcategories'),
    path('chapters/',ChapterListAPIView.as_view(),name='chapters'),
    path('boards/',BoardListAPIView.as_view(),name='boards'),
    path('question_histories/',QuestionHistoryListAPIView.as_view(),name='question_histories'),
    path('question_types/', QuestionTypeListAPIView.as_view(),name='question_types'),
]


