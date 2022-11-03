from django.urls import path, include

from Selldim.products import views

urlpatterns =[

    path('sell/', views.sell_product, name='sell'),

    path('details/', include([
        path('<slug:slug>/', views.product_details, name='product details'),
    ])),

    path('<pk>/', include([
        path('delete/', views.product_delete, name='product delete'),
        path('edit/', views.product_edit, name='product edit'),
    ])),

]