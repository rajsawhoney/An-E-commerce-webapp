# Generated by Django 2.2.9 on 2020-04-12 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20200412_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='itemCount',
            field=models.IntegerField(default=0, verbose_name='Item Count:'),
        ),
    ]