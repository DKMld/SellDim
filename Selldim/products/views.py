from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from Selldim.products.forms import ProductForm, EditProductForm
from Selldim.products.models import Products


def sell_product(request):

    form = ProductForm()

    if request.user.is_authenticated:

        if request.method == 'POST':

            form = ProductForm(request.POST, request.FILES)
            user_ads = Products.objects.filter(creator=request.user.pk)

            print(user_ads.count())

            if user_ads.count() >= 5:
                form = ProductForm()
                messages.error(request, 'You have exceeded the maximum ads per user (5),'
                                        ' please delete an add in order to create a new one!')

            if form.is_valid():
                instance = form.save()
                instance.creator = request.user
                instance.save()

        context = {
            "form": form,
            "user_is_auth": request.user.is_authenticated
        }

        return render(request, 'sell_products_page.html', context)

    messages.error(request, 'You must be logged in order to sell!')
    return redirect('login')


@login_required
def product_details(request, slug):

    if request.method == 'GET':
        product = get_object_or_404(Products, slug=slug)

        context = {
            'slug': slug,
            'product': product,
            'user_is_auth': request.user.is_authenticated,
        }

        if request.user.is_authenticated:
            return render(request, 'product_details.html', context)

        messages.error(request, 'You must be logged in to see other people ads!')
        return render(request, 'login.html')


@login_required
def product_edit(request, pk):
    product = Products.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditProductForm(instance=product)
    else:
        form = EditProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            context = {
                'user': request.user.username
            }
            return redirect('user ads', context)

    context = {
        'form': form,
        'user_is_auth': request.user.is_authenticated,
        'product': product,
    }

    return render(request, 'product_edit_page.html', context)


def product_delete(request, pk):
    product = get_object_or_404(Products, pk=pk)

    if product:
        product.delete()

        context = {
            'user': request.user.username
        }

        return redirect('user ads', context)

    return render(request, 'my_ads.html')
