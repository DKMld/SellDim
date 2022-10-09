from django.urls import path
from django.urls import include

from Selldim.common import views

urlpatterns = [
    path('', include([
        path('home/', views.home_page)
    ]))
]
