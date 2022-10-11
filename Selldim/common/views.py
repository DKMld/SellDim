from django.shortcuts import render, redirect

from django.contrib import messages


def home_page(request):

    if request.method == 'GET':
        return render(request, 'index.html')


def sell_product(request):

    if request.user.is_authenticated:
        return render(request, 'sell_products_page.html')
    elif not request.user.is_authenticated:
        messages.error(request, 'You must be logged in order to sell!')
        return redirect('login')
