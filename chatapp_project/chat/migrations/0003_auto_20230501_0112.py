# Generated by Django 2.1.7 on 2023-05-01 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20230418_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='summary',
            field=models.BinaryField(),
        ),
    ]