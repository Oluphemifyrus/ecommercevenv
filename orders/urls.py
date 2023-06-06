from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.add_customer, name='add_customer'),
    path('saveitems/<int:id>', views.save_item, name='save_item'),
    path('processpayment/', views.processpayment,  
          name='processpayment'),
    path('canceled/', views.payment_canceled, name='canceled'),
]

