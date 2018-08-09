from django.conf.urls import url
from .views import start_builder, select_parts, compare_item, configurations


urlpatterns = [
    url(r'^start/$', start_builder, name='start_builder'),
    url(r'^parts/$', select_parts, name='select_parts'),
    url(r'^compare/$', compare_item, name='compare_item'),
    url(r'^configurations/$', configurations, name='configurations'),
]