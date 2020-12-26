from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Message
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)
        depth = 1


class MessageSerializer(serializers.ModelSerializer):
    receiver_username = serializers.SerializerMethodField()
    sender_username = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ('id','subject', 'message', 'creation_date', 'sender_username', 'receiver_username',)

    def get_receiver_username(self, obj):
        return obj.receiver.username

    def get_sender_username(self , obj):
        return obj.sender.username

    def create(self, validated_data):
        sender_user = validated_data['sender_user']
        try:
            reciver_user = User.objects.get(username=validated_data['receiver_user'])
        except:
            raise serializers.ValidationError("not found the reciver user")
        return Message.objects.create(
            subject=validated_data['subject'],
            message=validated_data['message'],
            sender=validated_data['sender_user'],
            receiver=reciver_user
        )