from django.contrib import admin
from .models import Order
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('cart', 'order_status', 'shipping_total',
              'order_total')
    list_display = fields = ('order_id','cart_id', 'order_status', 'shipping_total',
                             'order_total',)
