from django.contrib import admin

from .models import Category, ProductType, Product, ProductImage



from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Product
        fields = '__all__'



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    # fieldsets = (
    #     (None, {
    #         "fields": (
    #             'name', 'thumbnail', 'product_count', 'product_type', 'product_tag', 'description', 'category', 'price_amount', 'old_price', 'discount', 'charge_taxes', 'rating1count', 'rating2count', 'rating3count', 'rating4count', 'rating5count', 'overall_rating',
    #         ),
    #     }),

    # )

    list_display = ['name', 'product_tag', 'product_count', 'updated_at', 'rating1count',
                    'rating2count', 'rating3count', 'rating4count', 'rating5count', 'overall_rating']

    # list_display_links=['name','slug','product_tag']

    list_filter = ['product_tag', 'product_type',
                   'category', 'charge_taxes', 'overall_rating', ]

    search_fields = ['name', 'product_type',
                     'category', 'product_tag', 'description']

    class Meta:
        model = Product


# Register your models here.
admin.site.register(Category)
# admin.site.register(Product,ProductAdmin) #already registered above using @admin.register()
admin.site.register(ProductType)
admin.site.register(ProductImage)
