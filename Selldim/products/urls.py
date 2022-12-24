from django.urls import path, include
from Selldim.products import views as product_views
from Selldim.common import views as common_views

urlpatterns = [

    path('sell/', product_views.sell_product, name='sell'),


    path('<slug:slug>/', include([
        path('details/', product_views.ProductDetails.as_view(), name='product details'),
    ])),


    path('<pk>/', include([
        path('delete/', product_views.ProductDelete.as_view(), name='product delete'),
        path('edit/', product_views.ProductEdit.as_view(), name='product edit'),
        path('like/', common_views.product_like, name='product like')
    ])),

]
