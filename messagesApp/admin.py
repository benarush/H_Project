from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Message._meta.get_fields() if f.one_to_many != True]
    search_fields = ('subject',)