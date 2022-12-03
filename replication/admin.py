from django.contrib import admin
from .models import Order, Order_copy

# Register your models here.
admin.site.register(Order)
admin.site.register(Order_copy)