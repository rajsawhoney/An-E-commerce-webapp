# Generated by Django 3.0.5 on 2020-07-06 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meme',
            name='meme',
        ),
        migrations.AddField(
            model_name='meme',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description:'),
        ),
        migrations.AddField(
            model_name='meme',
            name='pics',
            field=models.ManyToManyField(to='photos.Photo', verbose_name='photos'),
        ),
        migrations.AddField(
            model_name='meme',
            name='text',
            field=models.CharField(max_length=50, null=True, verbose_name='text desc'),
        ),
    ]
