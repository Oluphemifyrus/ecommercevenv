from django.urls import path
from . import views
from cart import cart
from cart import forms

app_name = 'eCommerceApp'   # app name

# pattern for the index page, all products and each product
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('productdetail/<int:id>/', views.product_detail, name='product_detail'),
]