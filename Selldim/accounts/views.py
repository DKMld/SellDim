from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from Selldim.common.views import home_page
from Selldim.accounts.forms import AccountsForm
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

    return redirect(home_page)


@csrf_protect
@login_required
def delete_user(request):
    pass


@login_required
def user_ads(request, username):

    if request.user.is_authenticated:

        user = request.user
        user_active_ads = Products.objects.filter(creator=user.pk)

        context = {'user': user,
                   'user_active_ads': user_active_ads,
                   'user_is_auth': request.user.is_authenticated,
                   }

        print(context)

        return render(request, 'my_ads.html', context)


@login_required
def profile_details(request, username):
    # TODO profile details page
    user = User.objects.filter(username=username)

    context = {
        'user': request.user,
        'user_is_auth': request.user.is_authenticated
    }

    return render(request, 'profile_details.html', context)
