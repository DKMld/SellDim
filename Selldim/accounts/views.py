from django.shortcuts import render
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
    pass


def delete_user(request):
    pass




