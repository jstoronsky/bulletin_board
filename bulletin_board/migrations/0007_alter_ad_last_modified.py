# Generated by Django 4.2.4 on 2023-11-09 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0006_ad_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='last_modified',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата последнего обновления'),
        ),
    ]
