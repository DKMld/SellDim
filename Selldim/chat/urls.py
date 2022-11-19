from django.urls import path
from Selldim.chat import views as chat_views

urlpatterns = [
    path('<str:room_name>', chat_views.room, name='room'),
    path('', chat_views.chat_room, name='room')
]
