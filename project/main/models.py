from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='author'
    )
    target = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='target'
    )
    text = models.CharField(max_length=500)

class GroupChat(models.Model):

    name = models.CharField(max_length=60)
    members = models.ManyToManyField(User)

class GroupChatMsg(models.Model):

    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='sender',
        null=True
    )
    group = models.ForeignKey(
        to=GroupChat,
        on_delete=models.CASCADE,
        related_name='group',
        null=True
    )
    text = models.CharField(max_length=500)

class UserDeco(models.Model):
    text = models.CharField(max_length=30, null=True, blank=True )
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        null=True
        )
