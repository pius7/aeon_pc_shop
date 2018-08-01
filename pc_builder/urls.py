from django.conf.urls import url
from .views import start_builder
from .views import select_parts

urlpatterns = [
    url(r'^start/$', start_builder, name='start_builder'),
    url(r'^parts/$', select_parts, name='select_parts'),
]