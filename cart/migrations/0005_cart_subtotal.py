# Generated by Django 2.2.9 on 2020-04-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20200412_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='subTotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Grand Total'),
        ),
    ]
