from django.urls import path
from user_profile.api.views import registration_api_view,LoginAPIView,profile_api_view,profile_api_update_view, DistrictListAPIView

app_name = 'user_profile'

urlpatterns=[
    path('register/',registration_api_view,name='register'),
    path('login/',LoginAPIView.as_view(),name='login'),
    path('profile/',profile_api_view, name='profile'),
    path('profile/update/',profile_api_update_view,name='update'),
    path('districts/',DistrictListAPIView.as_view(),name='districts'),
]