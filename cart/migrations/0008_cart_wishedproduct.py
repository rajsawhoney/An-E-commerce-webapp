# Generated by Django 2.2.9 on 2020-04-13 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20200413_1013'),
        ('cart', '0007_cart_itemcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='wishedProduct',
            field=models.ManyToManyField(blank=True, related_name='wish_list_product', to='product.Product', verbose_name='WishList'),
        ),
    ]
