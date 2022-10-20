from django.shortcuts import render, redirect
from django.contrib import messages
from Selldim.products.models import Products


def home_page(request):

    if request.method == 'GET':
        last_four_ads = Products.objects.filter().order_by('-id')[:8]

        context = {
            'last_four_ads': last_four_ads[:4],
            'last_eight_ads': last_four_ads[4::],
        }

        # context + 'user': request.user          # to add

        if request.user.is_authenticated:
            return render(request, 'index_logged.html', context)
        return render(request, 'index.html', context)


