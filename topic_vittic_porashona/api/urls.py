from django.urls import path

from topic_vittic_porashona.api.views import TopicVitticPorashonaListAPIView

app_name = 'topic_vittic_porashona'

urlpatterns =[
    path('list/', TopicVitticPorashonaListAPIView.as_view(), name='topic_vittic_porashona'),
]

