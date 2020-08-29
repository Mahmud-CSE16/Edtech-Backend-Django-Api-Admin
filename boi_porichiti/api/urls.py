from django.urls import path
from boi_porichiti.api.views import BoiListAPIView

app_name = 'boi_porichiti'

urlpatterns = [
    path('list/',BoiListAPIView.as_view(),name='boi_porichiti'),
]