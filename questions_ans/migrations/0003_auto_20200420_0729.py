# Generated by Django 2.2.9 on 2020-04-20 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions_ans', '0002_auto_20200419_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questions_ans.Question', verbose_name='Answer for Qn.:'),
        ),
    ]
