from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Message

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'chat/signup.html', {'form': form})

@login_required
def chat_home(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat/registered_users.html', {'users': users})

@login_required
def start_chat(request, user_id):
    receiver = User.objects.get(id=user_id)
    messages = Message.objects.filter(
        sender=request.user, receiver=receiver) | \
        Message.objects.filter(sender=receiver, receiver=request.user)
    return render(request, 'chat/conversation.html', {'receiver': receiver, 'messages': messages})
