from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'subTotal', 'added_on', ]


admin.site.register(CartItem)
