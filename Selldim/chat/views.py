from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from Selldim.accounts.models import ProfilePicture
from Selldim.chat.models import ChatMessage, Messages
from Selldim.products.models import Products


def chat_room(request):
    current_user = request.user
    user_list = [current_user.id]
    chat_group = ChatMessage.objects.filter(receiever__in=user_list)

    context = {
        'user_is_auth': request.user.is_authenticated,
        'receieved_messages': chat_group,
    }

    return render(request, 'chat_pages/chat_page.html', context)


def room(request, room_name, username):
    if not request.user.is_authenticated:
        return redirect('home page')

    current_user = User.objects.filter(username=request.user.username).get()
    current_user_image = None
    if ProfilePicture.objects.filter(user=current_user):
        current_user_image = ProfilePicture.objects.filter(user=current_user).get()

    other_user = User.objects.filter(username=username).get()
    other_user_image = None
    if ProfilePicture.objects.filter(user=other_user):
        other_user_image = ProfilePicture.objects.filter(user=other_user).get()

    product = Products.objects.filter(id=room_name).get()

    user_list = [other_user, current_user]
    current_chat_room = None
    if ChatMessage.objects.filter(room_name=room_name, sender__in=user_list, receiever__in=user_list):
        current_chat_room = ChatMessage.objects.filter(room_name=room_name, sender__in=user_list, receiever__in=user_list).get()
    messages = Messages.objects.filter(room_name=current_chat_room, sender__in=user_list, receiever__in=user_list)

    context = {
        'room_name': room_name,
        'request': request,
        'user_is_auth': request.user.is_authenticated,
        'messages': messages,
        'current_user': current_user,
        'current_user_image': current_user_image.user_picture,
        'other_user_image': other_user_image,
        'receiever': other_user.username,
        'product': product,

    }
    return render(request, 'chat_pages/messages_page.html', context)
