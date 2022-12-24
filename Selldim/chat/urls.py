from django.urls import path
from Selldim.chat import views as chat_views

urlpatterns = [
    path('<room_name>/<str:username>/', chat_views.chat_messages, name='send message'),
    path('', chat_views.chat_room, name='chat room'),
    path('delete/<room_name>/<sender>/', chat_views.delete_room, name='chat room delete')
]