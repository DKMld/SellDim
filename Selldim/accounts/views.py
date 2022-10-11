from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect

from Selldim.common.views import home_page

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

        user = authenticate(request, username=username, password=password)

        if user is not None:

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

    return redirect(home_page)


def delete_user(request):
    pass




