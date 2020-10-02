from django.urls import path
from blog.api.views import BlogListAPIView

app_name = 'blog'

urlpatterns = [
    path('list/',BlogListAPIView.as_view(),name='blog'),
]