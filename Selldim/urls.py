from django.contrib import admin
from django.urls import path
from django.urls import include

from Selldim.accounts import urls as accounts_urls
from Selldim.common import urls as common_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(accounts_urls)),
    path('', include(common_urls))

]