# Generated by Django 3.0.5 on 2020-04-25 11:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20200422_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
