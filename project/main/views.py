from django.shortcuts import render
from .forms import MessageForm, GroupMsgForm, GroupForm, ProfileForm
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Message, GroupChat, GroupChatMsg, UserDeco
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class MessageToUser(FormMixin, DetailView):

    model = User
    form_class = MessageForm
    template_name = 'user_chat.html'
    context_object_name = 'targetuser'
    
    def get_success_url(self) -> str:
        return reverse_lazy('detail', kwargs={'pk':self.get_object().id})
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = form.save(commit=False)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.target = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.all()
        return context
    
class UserList(ListView):

    model = User
    template_name = 'user_list.html'
    context_object_name = 'userlist'
    ordering_by = '-id'

class GroupList(ListView):

    model = GroupChat
    template_name = 'group_list.html'
    context_object_name = 'grouplist'
    ordering_by = '-id'

class GroupView(FormMixin, DetailView):

    model = GroupChat
    form_class = GroupMsgForm
    template_name = 'group_chat.html'
    context_object_name = 'targetchat'
    
    def get_success_url(self) -> str:
        return reverse_lazy('chatdetail', kwargs={'pk':self.get_object().id})
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = form.save(commit=False)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form):
        self.object = form.save(commit=False)
        print(self.get_object())
        self.object.group = self.get_object()
        print(self.request.user)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = GroupChatMsg.objects.all()
        return context
    
def ConnectToGroup(request, pk):
    chat = GroupChat.objects.get(pk=pk)
    chat.members.add(request.user)
    return redirect('/messages/group')

def DisconnectFromGroup(request, pk):
    chat = GroupChat.objects.get(pk=pk)
    chat.members.remove(request.user)
    return redirect('/messages/group')

class AddGroup(CreateView):
    model = UserDeco

    form_class = GroupForm

    template_name = 'addchat.html'

    success_url = reverse_lazy('chatlist')

class AddDeco(CreateView):
    model = UserDeco

    form_class = ProfileForm

    template_name = 'profile.html'

    success_url = reverse_lazy('updateprofile')
    

class UpdateDeco(UpdateView):
    model = UserDeco

    form_class = ProfileForm

    template_name = 'profile.html'

    success_url = reverse_lazy('updateprofile')