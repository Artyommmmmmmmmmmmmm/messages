from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import UserList, MessageToUser, GroupView, GroupList, ConnectToGroup, AddGroup, DisconnectFromGroup,\
    UpdateDeco, AddDeco

urlpatterns = [
    path('', UserList.as_view(), name='list'),
    path('<int:pk>', MessageToUser.as_view(), name='detail'),
    path('group/<int:pk>', GroupView.as_view(), name='chatdetail'),
    path('group/', GroupList.as_view(), name='chatlist'), 
    path('connect/<int:pk>', ConnectToGroup, name='connect'),
    path('addgroup', AddGroup.as_view(), name='addchat'),
    path('disconnect/<int:pk>', DisconnectFromGroup, name='disconnect'),
    path('addprofile', AddDeco.as_view(), name='addprofile'),
    path('updateprofile', UpdateDeco.as_view(), name='updateprofile'),
]