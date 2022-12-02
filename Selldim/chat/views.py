from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Selldim.accounts.models import ProfilePicture
from Selldim.chat.models import ChatMessage, Messages
from Selldim.products.models import Products


def chat_room(request):

    context = {
        'user_is_auth': request.user.is_authenticated,
    }
    return render(request, 'chat_pages/chat_page.html', context)

def room(request, room_name):
    if not request.user.is_authenticated:
        return redirect('home page')

    messages = ChatMessage.objects.filter(room_name=room_name)
    current_user = User.objects.filter(username=request.user.username).get()
    current_user_image = ProfilePicture.objects.filter(user=current_user).get()
    product = Products.objects.filter(id=room_name).get()


    context = {
        'room_name': room_name,
        'request': request,
        'user_is_auth': request.user.is_authenticated,
        'messages': messages,
        'current_user': current_user,
        'current_user_image': current_user_image.user_picture,
        'reciever': product.creator.username

    }
    return render(request, 'chat_pages/messages_page.html', context)


# def room(request, room_name):
#     if not request.user.is_authenticated:
#         return redirect('home page')
#
#     user = User.objects.filter(username=request.user.username).get()
#     current_user_image = ProfilePicture.objects.filter(user=user).get()
#
#     product = Products.objects.filter(id=room_name).get()
#     product_creator_image = None
#     if ProfilePicture.objects.filter(user=product.creator):
#         product_creator_image = ProfilePicture.objects.filter(user=product.creator)
#
#     # add_chat_user_list = [request.user, product.creator]

#     # msg_room = None
#     # if ChatMessage.objects.filter(room_name=room_name,):
#     #     msg_room = ChatMessage.objects.filter(room_name=room_name,)
#     #
#     # messages = None
#     # if msg_room:
#     #     messages = Messages.objects.filter(room_name=msg_room)
#
#     context = {
#         'room_name': room_name,
#         'request': request,
#         'user_is_auth': request.user.is_authenticated,
#         'messages': messages,
#         'current_user': user,
#         'current_user_image': current_user_image.user_picture,
#         'product': product,
#         'product_creator_image': product_creator_image,
#     }
#     return render(request, 'messages_page.html', context)



# def send_message(request, room_name):
#     user = User.objects.filter(username=request.user.username).get()
#     current_user_image = ProfilePicture.objects.filter(user=user).get()
#     product = Products.objects.filter(id=room_name).get()
#
#     add_chat_user_list = [request.user, product.creator]
#
#     msg_room = None
#     if ChatMessage.objects.filter(room_name=room_name, sender__in=add_chat_user_list, receiever__in=add_chat_user_list):
#         msg_room = ChatMessage.objects.filter(
#             room_name=room_name,
#             sender__in=add_chat_user_list,
#             receiever__in=add_chat_user_list).get()
#
#     messages = None
#     if msg_room:
#         messages = Messages.objects.filter(room_name=msg_room, sender__in=add_chat_user_list, receiever__in=add_chat_user_list)
#
#     context = {
#         'user_is_auth': request.user.is_authenticated,
#         'user': user,
#         'current_user_image': current_user_image.user_picture,
#         'product': product,
#         'receiever': product.creator.username,
#         'messages': messages,
#         'room_name': room_name,
#
#     }
#
#     return render(request, 'chat_pages/messages_page.html', context)
#
#
# def receieve_message(request, room_name, receiever):
#
#     user = User.objects.filter(username=request.user.username).get()
#     current_user_image = ProfilePicture.objects.filter(user=user).get()
#     product = Products.objects.filter(id=room_name).get()
#
#     add_chat_user_list = [request.user, product.creator]
#
#     receiever =receiever
#
#     receieved_messages = None
#     if ChatMessage.objects.filter(
#             room_name=room_name,  receiever__in=add_chat_user_list):
#
#         receieved_messages = ChatMessage.objects.filter(
#             room_name=room_name,  receiever__in=add_chat_user_list).get()
#
#         # print(receieved_messages)
#
#     print(receiever)
#
#     context = {
#         'user_is_auth': request.user.is_authenticated,
#         'user': user,
#         'current_user_image': current_user_image,
#         'product': product,
#         'receiever': receiever.username,
#         'room_name': room_name,
#         'receieved_messages': receieved_messages,
#
#     }
#     return render(request, 'chat_pages/messages_page.html', context)
