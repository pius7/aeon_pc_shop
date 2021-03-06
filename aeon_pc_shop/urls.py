"""aeon_pc_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home import urls as urls_home
from parts import urls as part_urls
from pc_builder import urls as builder_urls
from accounts import urls as accounts_urls
from .settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls, name=''),
    url(r'^', include(urls_home, namespace='home'), name='home'),
    url(r'^parts/', include(part_urls, namespace='part'), name='part'),
    url(r'^accounts/', include(accounts_urls, namespace='accounts'), name='accounts'),
    url(r'^builder/', include(builder_urls, namespace='builder'), name='builder'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
