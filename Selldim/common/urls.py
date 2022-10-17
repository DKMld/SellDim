from django.urls import path
from django.urls import include

from Selldim.common import views

urlpatterns = [
    path('', include([
        path('home/', views.home_page, name='home page'),

        # path('home/<username>'), views.user_profile, name='user profile',     # to add
        # may use include for all the functionality !!!

    ]))
]

