from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from . import views
app_name='shop'

urlpatterns = [

    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail'),
]
