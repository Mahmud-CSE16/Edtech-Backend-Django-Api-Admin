from django.urls import path

from question.api.views import mcq_question_api_view, McqQuestionListAPIView

app_name = 'question'

urlpatterns =[
    path('mcq_question/<pk>',mcq_question_api_view, name = 'mcq_question'),
    path('mcq_question/list/', McqQuestionListAPIView.as_view(), name='mcq_question_list'),
]

