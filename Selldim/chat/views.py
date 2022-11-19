from django.shortcuts import render, redirect


# Create your views here.

def chat_room(request):
    return render(request, 'blank_chat_page.html')

def room(request, room_name):
    if not request.user.is_authenticated:
        return redirect('home page')

    context = {
        'room_name': room_name,
        'request': request,
    }
    return render(request, 'messages_page.html', context)
