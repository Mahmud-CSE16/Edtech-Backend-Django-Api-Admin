from django.urls import path
from shop.api.views import ShopListAPIView

app_name = 'shop'

urlpatterns = [
    path('list/',ShopListAPIView.as_view(),name='shop'),
]