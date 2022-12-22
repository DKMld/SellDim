from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from django.views.static import serve

from Selldim.accounts import urls as accounts_urls
from Selldim.common import urls as common_urls
from Selldim.products import urls as product_urls
from Selldim.chat import urls as chat_urls
from Selldim.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(accounts_urls)),
    path('', include(common_urls)),
    path('product/', include(product_urls)),
    path('chat/', include(chat_urls)),


    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += \
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),\
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),


handler403 = "Selldim.common.views.error_403"
handler404 = "Selldim.common.views.error_404"
handler500 = "Selldim.common.views.error_500"
