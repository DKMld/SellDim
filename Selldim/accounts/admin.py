from django.contrib import admin

from Selldim.accounts.models import ProfilePicture, UserComments

class UserCommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sender', 'comment')
    list_filter = ('id', 'user', 'sender')


admin.site.register(ProfilePicture)
admin.site.register(UserComments, UserCommentsAdmin)