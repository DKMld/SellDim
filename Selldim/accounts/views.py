from django import views
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect

from django.views.generic import DeleteView

from Selldim.accounts.forms import AccountsForm, AccountsEditForm, AddProfilePicture
from Selldim.accounts.models import ProfilePicture
from Selldim.common.models import ProductLikes
from Selldim.products.models import Products


@csrf_protect
def register_user(request):
    form = AccountsForm()

    if request.method == "POST":
        form = AccountsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        messages.error(request, 'Username is already taken!')

    context = {
        'form': form,
    }

    return render(request, 'register.html', context)


@csrf_protect
def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pswrd')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            return redirect('home page')

        elif user is None:
            messages.success(request, 'Username or password is incorrect!')
            return render(request, 'login.html')

    context = {'user_is_auth': request.user.is_authenticated, }
    return render(request, 'login.html', context)


@csrf_protect
@login_required
def log_out_user(request):
    logout(request)

    return redirect('home page')


# @csrf_protect
# @login_required
# class ProfileDelete(DeleteView):
#     template_name = 'profile_details.html'
#     model = User
#     success_url = reverse_lazy('index')



@login_required
def user_ads(request, username):

    if request.user.is_authenticated:

        user = request.user
        user_active_ads = Products.objects.filter(creator=user.pk)

        context = {'user': user,
                   'user_active_ads': user_active_ads,
                   'user_is_auth': request.user.is_authenticated,
                   }

        return render(request, 'my_ads.html', context)


@login_required
def profile_details(request, username):
    user = User.objects.filter(username=username).get()
    form = AccountsEditForm(instance=user)

    if request.method == 'POST':
        form = AccountsEditForm(request.POST, instance=user)

        if form.is_valid().is_valid():
            form.save()

    context = {
        'user': user,
        'user_is_auth': request.user.is_authenticated,
        'form': form,

    }

    return render(request, 'profile_details.html', context)


def favourite_ads_user(request, username):
    user = request.user
    user_favourite_ads = ProductLikes.objects.filter(user=user.pk)

    print(user_favourite_ads)

    context = {
        'user': user,
        'user_is_auth': request.user.is_authenticated,
        'user_favourite_ads': user_favourite_ads,
    }

    return render(request, 'my_favourite_ads.html', context)
