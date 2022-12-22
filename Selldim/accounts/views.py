from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from Selldim.accounts.forms import AccountsForm, AccountsEditForm, AddProfilePicture, LeaveComment
from Selldim.accounts.models import ProfilePicture, UserComments
from Selldim.common.models import ProductLikes
from Selldim.products.models import Products


@csrf_protect
def register_user(request):
    form = AccountsForm()

    if request.method == "POST":
        form = AccountsForm(request.POST)
        if form.is_valid():
            form.save()

            username = request.POST.get('username')
            password = request.POST.get('password1')
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home page')

        messages.error(request, 'Username is already taken!')

    context = {
        'form': form,
    }

    return render(request, 'auth_pages/register.html', context)


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
            messages.error(request, 'Username or password is incorrect!')
            return render(request, 'auth_pages/login.html')

    context = {'user_is_auth': request.user.is_authenticated, }
    return render(request, 'auth_pages/login.html', context)


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
def profile_details(request, username):
    user = User.objects.filter(username=username).get()
    form = AccountsEditForm(instance=user)
    form_picture = AddProfilePicture(instance=user)

    if request.method == 'POST':
        form = AccountsEditForm(request.POST, instance=user)
        form_picture = AddProfilePicture(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            return redirect('login')

        if form_picture.is_valid():
            picture = form_picture.cleaned_data['user_picture']
            if not ProfilePicture.objects.filter(user=user):
                ProfilePicture.objects.create(user=user, user_picture=picture).save()
            ProfilePicture.objects.filter(user=user).delete()
            ProfilePicture.objects.create(user=user, user_picture=picture).save()

    user_picture = None
    if ProfilePicture.objects.filter(user=user):
        user_picture = ProfilePicture.objects.filter(user=user).get()

    context = {
        'user': user,
        'user_is_auth': request.user.is_authenticated,
        'form': form,
        'form_picture': form_picture,
        'user_picture': user_picture,
    }

    return render(request, 'account_pages/profile_details.html', context)


@login_required
def user_ads(request, username):
    user = request.user
    user_active_ads = Products.objects.filter(creator=user.pk)

    context = {
        'user': user,
        'user_active_ads': user_active_ads,
        'user_is_auth': request.user.is_authenticated,
    }

    return render(request, 'common_pages/my_ads.html', context)


@login_required
def favourite_user_ads(request, username):
    user = User.objects.filter(username=username).get()
    user_favourite_ads = ProductLikes.objects.filter(user=user.pk)

    context = {
        'user': user,
        'user_is_auth': request.user.is_authenticated,
        'user_favourite_ads': user_favourite_ads,
    }

    return render(request, 'common_pages/my_favourite_ads.html', context)


def other_users_ads(request, username):
    other_user = User.objects.filter(username=username).get()
    other_user_ads = Products.objects.filter(creator=other_user)

    other_user_picture = None
    if ProfilePicture.objects.filter(user=other_user):
        other_user_picture = ProfilePicture.objects.filter(user=other_user).get()

    comments = UserComments.objects.filter(user=other_user)

    form = LeaveComment()
    if request.method == 'POST':
        form = LeaveComment(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.sender = request.user
            data.user = other_user
            data.save()

    context = {
        'user_is_auth': request.user.is_authenticated,
        'add_count': other_user_ads.count(),
        'other_user_ads': other_user_ads,
        'other_user_picture': other_user_picture,
        'other_user': other_user,
        'comments': comments,
        'form': form,
    }

    return render(request, 'common_pages/other_user_ads_page.html', context)