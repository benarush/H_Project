from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from messagesApp.views import *

urlpatterns = [
    path('api/', api_overview , name="messages-api-overview"),
    path('api/my_details/', api_account_details, name="my-user-details"),
    path('api/create_message/', create_message, name="my-user-details"),
    path('api/delete_message/<str:pk>', delete_messages, name="my-user-details"),
    path('api/message_sent/', show_sent_messages, name="my-user-details"),
    path('api/message_receiver/', show_received_messages, name="my-user-details"),
    path('login/', obtain_auth_token, name="token-login"),

]
