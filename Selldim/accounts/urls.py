from django.urls import path
from django.urls import include

from Selldim.accounts import views

urlpatterns = [
    path('', include([
        path('register/', views.register_user, name='register'),
        path('login/', views.login_user, name='login'),
]))]

