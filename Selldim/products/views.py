from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Selldim.products.forms import ProductForm


def sell_product(request):
    form = ProductForm()
    if request.user.is_authenticated:

        if request.method == 'POST':

            form = ProductForm(request.POST, request.FILES)
            print(request.FILES)
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
