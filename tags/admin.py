from django.contrib import admin
from .models import ProductTag

# Register your models here.

@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    fields=('title','product')
