# Generated by Django 2.1.7 on 2023-05-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20230501_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='summary',
            field=models.CharField(max_length=200),
        ),
    ]
