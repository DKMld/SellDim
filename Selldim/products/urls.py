from django.urls import path, include
from Selldim.products import views

urlpatterns = [

    path('sell/', views.sell_product, name='sell'),

    path('details/', include([
        path('<slug:slug>/', views.ProductDetails.as_view(), name='product details'),
    ])),

    path('<pk>/', include([
        path('delete/', views.ProductDelete.as_view(), name='product delete'),
        path('edit/', views.ProductEdit.as_view(), name='product edit'),
    ])),

]