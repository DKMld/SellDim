from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect

from Selldim.accounts.forms import AccountsForm


@csrf_protect
def register_user(request):
    form = AccountsForm()

    if request.method == "POST":
        form = AccountsForm(request.POST)
        if form.is_valid():
            form.save()

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
            return render(request, 'index.html')

    context = {}

    return render(request, 'login.html')


def log_out_user(request):
    pass


def delete_user(request):
    pass




