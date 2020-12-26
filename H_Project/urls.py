from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from messagesApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name="my-admin-page"),
    path('messages/', include('messagesApp.urls')),
]
