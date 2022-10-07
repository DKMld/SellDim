from django.urls import path
from django.urls import include

from Selldim.accounts import views

urlpatterns = [
    path('', views.register_user)
]