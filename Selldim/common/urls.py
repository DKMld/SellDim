from django.urls import path
from django.urls import include


from Selldim.common import views

urlpatterns = [
    path('', include([
        path('home/', views.HomePage.as_view(), name='home page'),
        path('home/search/', views.product_search, name='product search'),
        path('home/search/<category>', views.product_search_by_category, name='product search by category'),
    ])),



    # path('product_like/<int:pk>/', views.product_like, name='product like')
]
