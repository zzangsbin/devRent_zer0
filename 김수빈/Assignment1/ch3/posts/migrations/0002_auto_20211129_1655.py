# Generated by Django 3.2.9 on 2021-11-29 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='writer',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('choice1', '일상'), ('choice2', '냠냠'), ('choice3', '기타')], default='', max_length=10),
        ),
    ]
