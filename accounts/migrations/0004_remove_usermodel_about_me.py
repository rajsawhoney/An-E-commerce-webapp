# Generated by Django 2.2.9 on 2020-04-20 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_usermodel_about_me'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='about_me',
        ),
    ]
