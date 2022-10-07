from django.contrib import admin
from django.urls import path
from django.urls import include

from Selldim.accounts import urls as accounts_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include(accounts_urls)),

]
