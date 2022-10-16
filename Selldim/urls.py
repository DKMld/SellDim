from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include

from Selldim.accounts import urls as accounts_urls
from Selldim.common import urls as common_urls
from Selldim.products import urls as product_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(accounts_urls)),
    path('', include(common_urls)),
    path('product/', include(product_urls))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
