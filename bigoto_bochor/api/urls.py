from django.urls import path
from bigoto_bochor.api.views import BigotoBochorListAPIView

app_name = 'bigoto_bochor'

urlpatterns = [
    path('list/',BigotoBochorListAPIView.as_view(),name='bigoto_bochor'),
]
