from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from .models import Message
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .serializers import UserSerializer , MessageSerializer
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

@receiver(post_save , sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@login_required
@api_view(('GET',))
def api_overview(request):
    """
    API Overview only H_Project user allowed to used this api
    for avoiding db overloading on prod site
    """
    api_urls = {
        'Get my user account details' : 'messages/api/my_details',
        'create new message': '/messages/api/create_message/',
        'Delete message': '/messages/api/delete_message/<str:pk>',
        'Get all sent Messages': '/messages/api/message_sent/',
        'Get all received Messages': '/messages/api/message_receiver/',
        'Token Auth': 'messages/login/',

    }
    return Response(api_urls)

@api_view(['POST'])
@authentication_classes([TokenAuthentication,])
def api_account_details(request, format=None):
    user = request.auth.user
    context = {'status': 'succeed', 'data': UserSerializer(user).data}
    return Response(context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication,])
def create_message(request):
    user = request.auth.user
    receiver_username = request.POST['receiver_username']
    serializer = MessageSerializer(data=request.data, many=False)
    if serializer.is_valid(raise_exception=True):
        serializer.save(sender_user=user, receiver_user=receiver_username)
        return Response({"status": "succeed"})
    else:
        return Response({"status": "failed"})


@api_view(['POST'])
@authentication_classes([TokenAuthentication,])
def show_sent_messages(request):
    user = request.auth.user
    serializer = MessageSerializer(Message.objects.all().filter(sender=user), many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication,])
def show_received_messages(request):
    user = request.auth.user
    serializer = MessageSerializer(Message.objects.all().filter(receiver=user), many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication,])
def delete_messages(request, pk):
    user = request.auth.user
    try:
        message = Message.objects.get(id=pk)
    except:
        return Response({"status": "not such of message"})
    if message.sender == user or message.receiver == user:
        message.delete()
        return Response({"status": "delete has been succeed"})
    return Response({"status": "permission denied"})
