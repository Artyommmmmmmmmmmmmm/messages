from django import forms
from .models import Message, GroupChat, GroupChatMsg, UserDeco

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserDeco
        fields = ['text', 'avatar']   
    
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']

class GroupMsgForm(forms.ModelForm):
    class Meta:
        model = GroupChatMsg
        fields = ['text']

class GroupForm(forms.ModelForm):
    class Meta:
        model = GroupChat
        fields = ['name']
