from django.urls import path

from question.api.views import question_api_view, QuestionListAPIView

app_name = 'question'

urlpatterns =[
    path('<pk>',question_api_view, name = 'question'),
    path('list/', QuestionListAPIView.as_view(), name='question_list'),
]

