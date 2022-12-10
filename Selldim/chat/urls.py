from django.urls import path
from Selldim.chat import views as chat_views

urlpatterns = [
    path('<room_name>/<str:username>/', chat_views.room, name='send message'),
    path('', chat_views.chat_room, name='chat room')
]