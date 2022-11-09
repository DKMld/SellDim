from django import views
from django.shortcuts import render, redirect
from Selldim.products.models import Products


class HomePage(views.View):
    def get(self, request):
        last_four_ads = Products.objects.filter().order_by('-id')[:8]
        user = request.user

        context = {
            'last_four_ads': last_four_ads[:4],
            'last_eight_ads': last_four_ads[4::],
            'user': user,
            'user_is_auth': request.user.is_authenticated,
        }

        return render(request, 'index.html', context)