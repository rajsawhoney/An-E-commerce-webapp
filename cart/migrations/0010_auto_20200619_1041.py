# Generated by Django 3.0.5 on 2020-06-19 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20200425_1656'),
        ('cart', '0009_auto_20200416_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='itemCount',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Item Count:')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart', verbose_name='Cart-ID')),
                ('product', models.ManyToManyField(blank=True, null=True, to='product.Product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'CartItem',
                'verbose_name_plural': 'CartItems',
            },
        ),
    ]
