from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from Selldim.products.forms import ProductForm
from Selldim.products.models import Products


def sell_product(request):

    form = ProductForm()

    if request.user.is_authenticated:

        if request.method == 'POST':

            form = ProductForm(request.POST, request.FILES)

            if form.is_valid():
                instance = form.save()
                instance.creator = request.user
                instance.save()

        context = {
            "form": form
        }
        return render(request, 'sell_products_page.html', context)

    messages.error(request, 'You must be logged in order to sell!')
    return redirect('login')


def product_details(request, slug):

    if request.method == 'GET':
        product = get_object_or_404(Products, slug=slug)

        context = {
            'slug': slug,
            'product': product
        }

        if request.user.is_authenticated:
            return render(request, 'product_details.html', context)

        messages.error(request, 'You must be logged in to see other people ads!')
        return render(request, 'login.html')
