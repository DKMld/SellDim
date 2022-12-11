import os

from django import views
from django.shortcuts import render, redirect

from Selldim import settings
from Selldim.common.forms import ProductSearchForm
from Selldim.common.models import ProductLikes
from Selldim.products.models import Products


class HomePage(views.View):
    def get(self, request):
        products = Products.objects.filter().order_by('-id').all()
        user = request.user

        context = {
            'last_four_ads': products[:4],
            'last_eight_ads': products[4::],
            'user': user,
            'user_is_auth': request.user.is_authenticated,
        }

        return render(request, 'common_pages/index.html', context)


def product_like(request, pk):
    product = Products.objects.filter(pk=pk).get()
    user = request.user
    product_liked_by_user = ProductLikes.objects.filter(product=product, user=user)

    if not product_liked_by_user:
        like = ProductLikes.objects.create(user=user, product=product)
        like.save()

    else:
        ProductLikes.objects.filter(user=user, product=product).delete()

    return redirect(get_product_url(request, product_id=product.pk))


def get_product_url(request, product_id):
    return request.META['HTTP_REFERER'] + f'#photo-{product_id}'


def product_search(request):
    if request.method == 'GET':
        products = Products.objects.filter().order_by('-id').all()
        search_form = ProductSearchForm(request.GET)
        search_pattern = None

        if search_form.is_valid():
            search_pattern = request.GET.get('search')

        if search_pattern:
            products = products.filter(product_name__icontains=search_pattern)

        context = {
            'user_is_auth': request.user.is_authenticated,
            'products': products
        }

        return render(request, 'product_pages/product_search_page.html', context)


def product_search_by_category(request, category):
    products = Products.objects.filter(category=category)

    context = {
        'user_is_auth': request.user.is_authenticated,
        'products': products,
    }

    return render(request, 'product_pages/product_search_page.html', context)