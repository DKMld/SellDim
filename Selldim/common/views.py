from django.shortcuts import render, redirect
from django.contrib import messages


def home_page(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'index_logged.html')
        return render(request, 'index.html')


