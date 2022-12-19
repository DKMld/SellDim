from django.contrib import admin

from Selldim.chat.models import ChatMessage,Messages


class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ("id", 'timestamp', 'room_name', 'sender', 'receiever')
    list_filter = ('id', 'timestamp', 'room_name', 'sender', 'receiever')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'timestamp', 'message')
    list_filter = ('id', 'timestamp', 'room_name')


admin.site.register(ChatMessage, ChatMessageAdmin)
admin.site.register(Messages, MessageAdmin)