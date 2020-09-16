"""mathbyrony URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('',views.IndexView.as_view()),
    path('pdf/',views.showpdf,name="showpdf"),

    # REST FRAMEWORK URLs
    path('api/question/',include('question.api.urls','question')),
    path('api/user/',include('user_profile.api.urls','user_profile')),
    path('api/common/',include('common.api.urls','common')),
    path('api/notification/',include('notification.api.urls','notification')),
    path('api/bigoto_bochor/',include('bigoto_bochor.api.urls','bigoto_bochor')),
    path('api/boi/',include('boi_porichiti.api.urls','boi_porichiti')),
    path('api/shop/',include('shop.api.urls','shop')),
    path('api/goniter_itihash/',include('goniter_itihash.api.urls','goniter_itihash')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

