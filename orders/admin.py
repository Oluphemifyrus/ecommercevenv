from django.contrib import admin
from .models import Customer, OrderItem

# Register your models here.

admin.site.register(OrderItem)

@admin.register(Customer)

