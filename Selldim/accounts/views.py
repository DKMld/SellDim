from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
import Selldim.common.views
from Selldim.accounts.forms import AccountsForm


@csrf_protect
def register_user(request):
    form = AccountsForm()

    if request.method == "POST":
        form = AccountsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
        messages.error(request, 'Username is already taken!')

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pswrd')
        print(password)
        print(username)

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print('user is not none!!!!!')
            login(request, user)
            context = {'user': user}
            return render(request, 'index_logged.html', context)
        elif user is None:
            messages.success(request, 'Username or password is incorrect!')
            return render(request, 'login.html')

    context = {}
    return render(request, 'login.html')


def log_out_user(request):
    logout(request)
    return ...


def delete_user(request):
    pass




