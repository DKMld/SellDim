from django import views
from django.shortcuts import render, redirect

from Selldim.common.models import ProductLikes
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


def product_like(request, pk):
    product = Products.objects.filter(pk=pk).get()
    user = request.user
    product_liked_by_user = ProductLikes.objects.filter(product=product, user=user)

    if not product_liked_by_user:
        like = ProductLikes.objects.create(user=user, product=product)
        like.save()

    else:
        ProductLikes.objects.filter(user=user, product=product).delete()

    return redirect(get_photo_url(request, product_id=product.pk))


def get_photo_url(request, product_id):
    return request.META['HTTP_REFERER'] + f'#photo-{product_id}'
