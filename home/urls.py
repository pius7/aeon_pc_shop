from django.conf.urls import url
from .views import home, about
from accounts.views import logout

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^about/$', about, name='about'),
]