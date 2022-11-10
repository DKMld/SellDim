from django.urls import path
from django.urls import include

from Selldim.accounts import views
from Selldim.common import views as common_views

urlpatterns = [
    path('', include([
        path('register/', views.register_user, name='register'),
        path('login/', views.login_user, name='login'),
        path('', views.log_out_user, name='log out'),


    ])),
    path('profile/<username>/', include([
            path('my_ads/', views.user_ads, name='user ads'),
            path('profile_details/', views.profile_details, name='profile details'),
    ]))


]

# path('home/<username>'), views.user_profile, name='user profile',
