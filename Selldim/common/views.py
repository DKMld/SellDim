import random

from django.shortcuts import render, redirect
from django.contrib import messages

from Selldim.products.models import Products


def home_page(request):

    if request.method == 'GET':
        last_five_ads = Products.objects.filter().order_by('-id')[:4]
        items = list(Products.objects.all())
        random_items = random.sample(items, 5)

        context = {
            'last_five_ads': last_five_ads,
            'random_items': random_items,
        }

        # context + 'user': request.user          # to add

        if request.user.is_authenticated:
            return render(request, 'index_logged.html', context)
        return render(request, 'index.html', context)


