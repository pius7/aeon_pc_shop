from django.conf.urls import url
from .views import view_account, register, login


urlpatterns = [
   url(r'^/', view_account,  name='view_account'),
   url(r'^register/', register,  name='register'),
   url(r'^login/', login,  name='login'),
   
]