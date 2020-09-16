from django.urls import path
from goniter_itihash.api.views import GoniterItihashListAPIView

app_name = 'goniter_itihash'

urlpatterns = [
    path('list/',GoniterItihashListAPIView.as_view(),name='goniter_itihash'),
]