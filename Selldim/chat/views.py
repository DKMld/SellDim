from django.shortcuts import render

# Create your views here.

def chatPage(request):
    return render(request, 'messages_page.html')