# Generated by Django 2.2.9 on 2020-04-20 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions_ans', '0006_auto_20200420_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionans',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questions_ans.QuestionAns', verbose_name='Answers'),
        ),
    ]
