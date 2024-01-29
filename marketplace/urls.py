"""
URL configuration for marketplace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from marketplace_api import views

from marketplace_api.views import ProductView, CategoryView

from rest_framework import routers
route= routers.DefaultRouter()
route.register("productview",ProductView, basename='productview')
route.register("categoryview",CategoryView, basename='categoryview')



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('auth/', include('djoser.urls')),
    #path('auth/', include('djoser.urls.jwt')),

    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('accounts.urls')),
    path('profile/', include('marketplace_api.urls')),
    path('api/',include (route.urls)),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]

