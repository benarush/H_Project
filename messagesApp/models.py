from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Message(models.Model):
    subject = models.CharField(max_length=100, unique=True)
    message = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='receiver')

    def __str__(self):
        return f"<Message : subject -> {self.subject} , sender -> {self.sender}" \
               f"receiver -> {self.receiver}>"
