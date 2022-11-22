from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Selldim.accounts.models import ProfilePicture
from Selldim.chat.models import ChatMessage


def chat_room(request):
    context = {
        'user_is_auth': request.user.is_authenticated
    }
    return render(request, 'chat_page.html', context)


def room(request, room_name):
    if not request.user.is_authenticated:
        return redirect('home page')

    messages = ChatMessage.objects.filter(room_name=room_name)
    current_user = User.objects.filter(username=request.user.username).get()
    current_user_image = ProfilePicture.objects.filter(user=current_user).get()



    context = {
        'room_name': room_name,
        'request': request,
        'user_is_auth': request.user.is_authenticated,
        'messages': messages,
        'current_user': current_user,
        'current_user_image': current_user_image.user_picture,
    }
    return render(request, 'messages_page.html', context)
