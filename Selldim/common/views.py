from django.shortcuts import render, redirect
from django.contrib import messages


def home_page(request):

    if request.method == 'GET':
        return render(request, 'index.html')


