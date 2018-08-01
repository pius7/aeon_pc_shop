from django.conf.urls import url
from .views import show_parts

urlpatterns = [
    url(r'^$', show_parts, name='show_parts'),
]