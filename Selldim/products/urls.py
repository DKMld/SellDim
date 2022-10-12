from django.urls import path

from Selldim.products import views

urlpatterns =[
    path('sell/', views.sell_product, name='sell'),
]