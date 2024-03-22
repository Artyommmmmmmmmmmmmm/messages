from django.contrib import admin
from .models import Message, GroupChat, GroupChatMsg, UserDeco
# Register your models here.
admin.register(Message)
admin.register(GroupChat)
admin.register(GroupChatMsg)
admin.register(UserDeco)