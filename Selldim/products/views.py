from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from Selldim.common.models import ProductLikes
from Selldim.products.forms import ProductForm, EditProductForm
from Selldim.products.models import Products
from django import views


def sell_product(request):

    form = ProductForm()

    if request.user.is_authenticated:

        if request.method == 'POST':

            form = ProductForm(request.POST, request.FILES)
            user_ads = Products.objects.filter(creator=request.user.pk)

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
        messages.success(request, 'Add added successfully!')
        return render(request, 'sell_products_page.html', context)

    messages.error(request, 'You must be logged in order to sell!')
    return redirect('login')


# @method_decorator(login_required, name='dispatch')
class ProductDetails(views.View):
    def get(self, request, *args, **kwargs):

        product = get_object_or_404(Products, slug=self.kwargs['slug'])
        product_liked_by_user = None

        if request.user.is_authenticated:
            product_liked_by_user = ProductLikes.objects.filter(product=product, user=request.user)

        context = {
            'slug': self.kwargs['slug'],
            'product': product,
            'user_is_auth': request.user.is_authenticated,
            'product_liked_by_user': product_liked_by_user,
        }

        return render(request, 'product_details.html', context)


@method_decorator(login_required, name='dispatch')
class ProductEdit(views.View):

    def get(self, request, *args, **kwargs):
        product = Products.objects.filter(pk=self.kwargs['pk']).get()
        form = EditProductForm(instance=product)

        context = {
            'form': form,
            'user_is_auth': request.user.is_authenticated,
            'product': product,
        }

        return render(request, 'product_edit_page.html', context)

    def post(self, request, *args, **kwargs):
        product = Products.objects.filter(pk=self.kwargs['pk']).get()
        form = EditProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            context = {
                'user': request.user.username
            }
            return redirect('user ads', context)


@method_decorator(login_required, name='dispatch')
class ProductDelete(views.View):

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Products, pk=self.kwargs['pk'])

        if product:
            product.delete()

            context = {
                'user': request.user.username
            }

            return redirect('user ads', context)

        return render(request, 'my_ads.html')
