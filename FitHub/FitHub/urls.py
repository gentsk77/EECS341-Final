"""FitHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from profile import views as profile_views

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', include('profile.urls')),
    #path('accounts/profile/', include('profile.urls')),
    path('signup', profile_views.signup, name='signup'),
    path('admin/', admin.site.urls),
    # url(r'^$', include('profile.urls')),
    path('', include('landing.urls')),
]