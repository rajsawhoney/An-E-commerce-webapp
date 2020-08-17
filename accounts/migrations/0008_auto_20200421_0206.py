# Generated by Django 3.0.5 on 2020-04-20 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200421_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='about_me',
            field=models.TextField(blank=True, default='I am a good person!', verbose_name='About me:'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='qualifications',
            field=models.TextField(blank=True, default="Bachelor's in Engineering", verbose_name='Your Qualifications'),
        ),
    ]
