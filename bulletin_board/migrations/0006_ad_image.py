# Generated by Django 4.2.4 on 2023-11-09 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0005_rename_advertisement_ad'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ads/', verbose_name='аватар пользователя'),
        ),
    ]
