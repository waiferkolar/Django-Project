from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="product-home"),
    path('single/product',views.singProduct,name="product-single")
]
