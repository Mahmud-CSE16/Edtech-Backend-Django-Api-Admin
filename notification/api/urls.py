from django.urls import path
from notification.api.views import NotificationListAPIView

app_name = 'notificaton'

urlpatterns = [
    path('list/',NotificationListAPIView.as_view(),name='notifications'),
]
